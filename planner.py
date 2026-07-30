"""Deterministic planning rules for Stuck Label Rescue."""

SURFACES = {
    "Glass or glazed ceramic": {"heat": True, "oil": True, "soak": True, "risk": "low"},
    "Bare stainless steel": {"heat": True, "oil": True, "soak": True, "risk": "low"},
    "Painted or coated metal": {"heat": False, "oil": True, "soak": False, "risk": "medium"},
    "Hard plastic": {"heat": False, "oil": True, "soak": False, "risk": "medium"},
    "Finished wood": {"heat": False, "oil": False, "soak": False, "risk": "high"},
    "Paper or cardboard": {"heat": False, "oil": False, "soak": False, "risk": "high"},
}


def build_plan(surface: str, label: str, age: str, priority: str) -> dict[str, object]:
    """Return a bounded removal sequence whose steps depend on every choice."""
    facts = SURFACES[surface]
    patient = priority == "Protect the item"
    fresh = age == "Fresh (under a week)"
    paper_label = label == "Paper label"
    steps: list[str] = []

    if surface == "Paper or cardboard":
        steps.append("Lift one corner with a clean, dry fingernail; keep the pull almost parallel to the surface.")
        steps.append("Pause every 2–3 cm and roll loosened adhesive inward with a clean fingertip.")
    elif surface == "Finished wood":
        steps.append("Warm the label only with your palm for 30 seconds, then test a corner with a plastic card.")
        steps.append("Peel slowly with the grain; rub remaining tack into small rolls with a dry cloth.")
    elif facts["soak"] and paper_label:
        duration = "10 minutes" if fresh else "20 minutes"
        steps.append(f"Cover the label with a warm, wet cloth for {duration}; do not use boiling water.")
        steps.append("Slide a plastic card under the softened paper and wipe away loose fibers.")
    else:
        steps.append("Lift a corner with a plastic card and peel low and slow, keeping the strip close to the surface.")
        if facts["heat"]:
            steps.append("If it resists, use warm—not hot—air for 20 seconds from an arm’s length away, then retry.")

    if facts["oil"] and not fresh:
        dwell = "5" if patient else "2"
        steps.append(f"Patch-test one drop of cooking oil; if unchanged after {dwell} minutes, massage it into residue and wipe clean.")
    elif facts["oil"]:
        steps.append("For leftover tack, patch-test a drop of cooking oil, rub for 30 seconds, then wash with dish soap.")
    elif not paper_label:
        steps.append("Roll remaining adhesive with a clean thumb; avoid soaking or solvent.")

    finish = {
        "Glass or glazed ceramic": "Wash with dish soap, rinse, and dry.",
        "Bare stainless steel": "Wash with dish soap and wipe with the grain.",
        "Painted or coated metal": "Remove oily residue with diluted dish soap; dry immediately.",
        "Hard plastic": "Wash briefly with mild dish soap; do not leave oil sitting on the plastic.",
        "Finished wood": "Buff dry immediately; stop without adding liquid if tack remains.",
        "Paper or cardboard": "Let the area rest flat and dry; accept faint residue rather than thinning the surface.",
    }[surface]
    steps.append(finish)

    stop = {
        "low": "Stop if the surface becomes too hot to touch or a tool begins to scratch.",
        "medium": "Stop immediately if color transfers, gloss changes, plastic softens, or coating lifts.",
        "high": "Stop at the first sign of fiber lift, finish dulling, color transfer, or a darkened patch.",
    }[str(facts["risk"])]
    return {
        "steps": steps,
        "stop": stop,
        "first_action": "Gather a plastic card, soft cloth, mild dish soap, and a timer; then test the least visible corner.",
        "badge": f"{len(steps)}-step {('surface-first' if patient else 'faster')} plan",
    }
