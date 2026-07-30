# Product Report — Stuck Label Rescue

## Value hypothesis

“The user will use this when a label or tape is stuck to an item they want to
keep. It helps by turning the surface, label, age, and damage tolerance into a
bounded removal sequence with stop signals. It is better than a generic search,
note, or checklist because the advice changes with the material and tells the
user when preserving the item matters more than removing every trace.”

- Trigger: a person is about to remove a stubborn label without damaging its surface.
- Primary interaction: choose surface, label type, age, and priority.
- Meaningful choices: six surfaces, two label types, two ages, two priorities.
- Immediate feedback: a labeled, surface-aware sequence appears on submit.
- Useful output: ordered steps, finish guidance, explicit stop rule, and first action.
- Concrete next action: gather the small kit and patch-test a hidden corner.
- Reason to return: different household objects and adhesives require different plans.
- New-case behavior: one button clears the result while keeping the tool ready.

## Exactly three candidates

1. When a person has a stubborn label on an item worth keeping, they need help
   to remove it without harming the surface, but existing tools are generic
   search results that mix incompatible solvents and materials.
   Target: household reusers and thrift shoppers. Interaction: surface/label/
   age/priority choices. Output: removal sequence plus stop rule. Next action:
   patch-test the least visible corner. Repeat use: every object differs.
   Test: deterministic rule tests and AppTest scenarios.
   Scores (0–5): usefulness 4.6, specificity 4.8, novelty 4.1, clarity 4.7,
   agency 4.4, result quality 4.5, next-action quality 4.5, repeat-use 4.0,
   interaction 4.2, feasibility 4.8, testability 4.8. Average: 4.49.
2. When a person must leave a temporary instruction sign in a shared space,
   they need help to make it readable at the right distance without writing a
   wall of text, but design tools are too large. Target: small event hosts.
   Interaction: distance, viewing time, lighting, message components. Output:
   a constrained sign layout. Next action: copy the layout. Repeat use: new
   events. Test: layout constraints. Scores: 4.0, 4.2, 3.8, 4.3, 3.7, 3.8,
   4.0, 3.2, 3.8, 4.7, 4.5. Average: 4.00. Rejected: result quality below 4.
3. When a person stores an oddly shaped fragile item for a few months, they
   need help to choose supports and orientation, but moving checklists ignore
   object geometry. Target: renters and collectors. Interaction: material,
   shape, weak points, storage conditions. Output: support map and inspection
   cadence. Next action: perform a stability test. Repeat use: occasional.
   Test: rule matrix. Scores: 4.1, 4.4, 4.0, 3.9, 3.6, 4.0, 3.8, 3.1, 3.7,
   4.2, 4.3. Average: 3.92. Rejected: clarity and repeat use below thresholds.

Selected candidate: **Stuck Label Rescue**.

## Product review

- Version 1 weakness: plans distinguished surfaces but did not tell the user
  when to stop, risking over-treatment of delicate finishes.
- Iteration 1: added surface-specific stop signals and a conservative patch test.
- Review weakness: the outcome still lacked a clear transition from reading to doing.
- Iteration 2: added a persistent “Do this now” kit/action and explicit new-case reset.
- No third iteration was needed.

Final scores: usefulness 4.6; specificity 4.7; clarity 4.6; agency 4.3;
interaction quality 4.2; result quality 4.6; next-action quality 4.5;
repeat-use potential 4.0; visual coherence 4.2; memorability 4.1. Average: 4.38.

Two reviewed scenarios: an old paper label on glass produces a warm wet-cloth
and oil sequence; fresh plastic film on finished wood produces dry, with-grain
steps and finish-specific stop signals.
