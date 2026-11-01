"""kitsuneOS bench capture triage — model-pinned reads for KRI firmware rounds.

Drafted on the Pocket Forge bench (⚡ Piko). Input is a verbatim USB CDC
serial capture from the IRIS DVI board (Pimoroni Feather RP2350 HSTX)
plus a mode selector:

    mode="triage"  — one capture, one fixed verdict block
    mode="debug"   — ranked hypotheses + cheapest discriminating bench test
    mode="ab"      — same capture through BOTH models, verdicts side by side

Models are pinned per call. `mistral-large-latest` should resolve to
Mistral Large 4 today — pin a dated model id from
https://docs.mistral.ai/models in the environment variables (or the
input) once validated, so a future `-latest` rotation cannot silently
swap the model under a running bench program.
"""

import asyncio
import os
from typing import Literal

from pydantic import BaseModel

import mistralai.workflows as workflows

# Pinned models. Override per deployment via env, per execution via input.
TRIAGE_MODEL = os.environ.get("TRIAGE_MODEL", "mistral-large-latest")
DEBUG_MODEL = os.environ.get("DEBUG_MODEL", "mistral-large-latest")

TRIAGE_INSTRUCTIONS = """You are the kitsuneOS bench triage agent for KRI.

You receive verbatim USB CDC serial captures from a Pimoroni Feather RP2350
HSTX board ("IRIS DVI") running kitsuneOS debug bins. Debug bins print a 1 Hz
status line over USB CDC. Read captures BY FIELDS, not prose.

Classify the round: build failure / flash failure / boot failure / UART
silent / runtime fault / pass. If the question concerns the DVI monitor,
report what the monitor shows (dark / "no signal" OSD / "out of range" OSD /
bars / flickers) with timing relative to events in the capture.

Answer with exactly this verdict block and nothing else:
STATUS: <one of the classifications above>
EVIDENCE: <exact quoted lines from the capture that justify it>
TIMING: <events vs. seconds-since-capture-start>
NEXT-ROUND: <one concrete bench action>

Never invent lines that are not present in the capture. Terse and factual:
verdicts land in PROJECT-STATUS.md.
"""

DEBUG_INSTRUCTIONS = """You are the kitsuneOS debug agent for KRI, pinned to
Mistral Large 4.

You reason over captures from the Tasogane stack: the Shell-Soul UART
protocol (kitsunebios <-> kitsuneOS), the Zeus VM and Hercules HAL, KMOD
loading with CRC32 verification, and the recursive multi-strip LED handler
architecture (extend it; never propose parallel mechanisms).

Given a capture and a triage verdict, produce AT MOST three ranked
hypotheses, each with the cheapest bench test that would discriminate it.
Respect the three-repo split: Shell logic lives in kitsunebios, prop logic in
kitsuneOS/KMOD, physical specifics in Project-Kogane. Flag any proposed fix
that crosses those layers. End with exactly one recommended next action,
not an essay."""


class TriageInput(BaseModel):
    """Input for one bench triage round.

    - capture: verbatim serial capture (115200 baud, USB CDC), unfiltered.
    - mode: "triage", "debug", or "ab".
    - hypothesis: optional working hypothesis (used in debug mode).
    - triage_model / debug_model: optional per-execution model overrides,
      taking precedence over the deployment environment variables.
    """

    capture: str
    mode: Literal["triage", "debug", "ab"] = "triage"
    hypothesis: str | None = None
    triage_model: str | None = None
    debug_model: str | None = None


def _completion(model: str, instructions: str, prompt: str) -> str:
    """Run one pinned-model chat completion and return the raw reply text.

    On managed deployments the worker runs with a platform-injected
    service-account token, which the Mistral SDK picks up automatically;
    the explicit key fallback covers local bench runs.
    """
    from mistralai.client import Mistral

    client = Mistral(api_key=os.environ.get("MISTRAL_API_KEY"))
    response = client.chat.complete(
        model=model,
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )
    return response.choices[0].message.content or ""


@workflows.activity()
async def triage_read(capture: str, model: str) -> str:
    """Triage read: capture in, fixed verdict block out."""
    return _completion(model, TRIAGE_INSTRUCTIONS, capture)


@workflows.activity()
async def debug_read(capture: str, model: str, hypothesis: str | None) -> str:
    """Debug read: capture plus optional hypothesis in, ranked analysis out."""
    prompt = f"Hypothesis under test: {hypothesis or 'none yet'}\n\nCapture:\n{capture}"
    return _completion(model, DEBUG_INSTRUCTIONS, prompt)


@workflows.workflow.define(
    name="kitsune-bench-triage",
    workflow_display_name="kitsuneOS Bench Triage",
    workflow_description=(
        "Parses kitsuneOS USB CDC bench captures into fixed verdict blocks, "
        "with model-pinned debug reads and a side-by-side A/B mode."
    ),
)
class BenchTriageWorkflow:
    """Route one bench capture through the model-pinned readers."""

    @workflows.workflow.entrypoint
    async def run(self, input: TriageInput) -> str:
        if input.mode == "triage":
            return await triage_read(input.capture, input.triage_model or TRIAGE_MODEL)
        if input.mode == "debug":
            return await debug_read(
                input.capture, input.debug_model or DEBUG_MODEL, input.hypothesis
            )
        # "ab": the honest Le Chonk test — same capture, both readers, no mercy.
        triage_model = input.triage_model or TRIAGE_MODEL
        debug_model = input.debug_model or DEBUG_MODEL
        triage_verdict, debug_verdict = await asyncio.gather(
            triage_read(input.capture, triage_model),
            debug_read(input.capture, debug_model, input.hypothesis),
        )
        return (
            f"--- TRIAGE ({triage_model}) ---\n{triage_verdict}\n\n"
            f"--- DEBUG ({debug_model}) ---\n{debug_verdict}"
        )
