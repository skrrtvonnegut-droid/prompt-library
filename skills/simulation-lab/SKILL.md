# Universal Simulation Lab

## Purpose

Model a bounded system through time so that the user can inspect plausible consequences, interacting incentives, hidden dependencies, failure modes, second- and third-order effects, and decision branches before acting in the real world.

Use this skill when the task is better represented as **state + actors + rules + uncertainty + events + time -> consequences** than as a static question. The skill is intentionally domain-neutral: it can support technical architecture, operations, incidents, organizations, personal decisions, games, narratives, strategy, and other dynamic systems.

Simulation is not prediction. The skill builds the smallest useful world model needed to expose consequences that would otherwise be difficult to see.

## Use When

Use this skill when the user asks to:

- simulate, tabletop, stress-test, play out, branch, or run a scenario forward;
- compare several possible futures from one decision point;
- inspect downstream consequences of a proposed change;
- model stakeholder behavior under differing incentives or information;
- red-team a design, process, plan, or decision;
- explore cascading failures or operational degradation;
- reason across a meaningful time horizon rather than only at the initial state;
- test a narrative or strategic choice for consistency and consequences;
- explore how a system behaves under explicit assumptions.

Natural-language invocation is preferred. The user should not need to supply a formal schema.

## Do Not Use When

Do not use this skill when:

- the user only needs a factual answer with no dynamic scenario;
- the request is a straightforward calculation that does not benefit from stateful modeling;
- the user wants a real-world action executed rather than modeled;
- a domain-specific analytical tool can provide an authoritative answer directly and no scenario reasoning is needed;
- the task would require pretending to know private thoughts, intentions, future events, or unavailable evidence;
- the request depends on unsupported precision that cannot be grounded in defensible data or distributions.

A simulated action is never an approval to perform the corresponding real action.

## Inputs

### Required

- **Scenario or decision** — the system, change, incident, choice, or situation to model.

### Optional

- **Objective** — what the user wants to learn, protect, optimize, or compare.
- **Initial state** — known facts about the starting condition.
- **Actors** — people, teams, systems, adversaries, characters, or agents whose behavior matters.
- **Constraints** — technical, financial, organizational, physical, narrative, ethical, or temporal limits.
- **Time horizon** — minutes, days, months, years, turns, scenes, or another appropriate progression.
- **Branches** — alternatives the user explicitly wants compared.
- **Success/failure criteria** — conditions that determine whether a branch is desirable.
- **Source material** — files, documents, connected data, current public information, code, datasets, diagrams, or prior analysis.

If useful information is missing, proceed with explicit assumptions rather than demanding unnecessary specification.

## Dependencies

### Required dependencies

None beyond a reasoning-capable runtime.

### Optional enhancements

Use available tools when they materially improve grounding or computation, for example:

- authoritative documentation or current web sources for changing external facts;
- connected knowledge systems for the actual current state of a project or environment;
- uploaded files for architecture, policy, source, or data evidence;
- code execution or numerical tools for defensible quantitative simulation;
- domain engines for authoritative verification, such as a chess engine for tactical correctness.

### Safe fallback

When a dependency is unavailable, continue qualitatively if the scenario remains useful and clearly identify what could not be grounded or verified.

## Classification

The canonical skill body is **Public**.

Invocation-time source material inherits the classification and handling rules of the active runtime. Do not copy private, employer-confidential, secret, or otherwise restricted invocation data into the public registry.

Simulation transcripts are ephemeral by default. Durable outputs should be promoted only when the user requests persistence or the active runtime has an established, authorized routing policy.

## Simulation Model

Normalize substantial scenarios internally around this conceptual model. Do not require the user to fill it out directly.

```yaml
scenario:
  objective:
  domain:
  scope:
  horizon:
  granularity:

initial_state:
  known_facts: []
  assumptions: []
  unknowns: []
  constraints: []

actors:
  - name:
    role:
    goals: []
    capabilities: []
    incentives: []
    information: []
    constraints: []

environment:
  rules: []
  dependencies: []
  resources: []
  external_forces: []

events:
  scheduled: []
  hypothetical: []

metrics:
  success_conditions: []
  failure_conditions: []
  warning_signals: []

simulation:
  mode:
  branches:
  rounds:
  stop_conditions: []
```

Use only the fields needed for the scenario.

## Evidence States

Keep major claims internally distinguishable as:

- **FACT** — retrieved or supplied evidence about the real starting state.
- **ASSUMPTION** — a working condition introduced to make modeling possible.
- **INFERENCE** — a consequence derived from facts and assumptions.
- **HYPOTHETICAL** — an intentionally invented scenario event or branch.
- **UNKNOWN** — material information that is unavailable or unresolved.

Never silently promote an assumption, inference, or hypothetical event into fact.

## Simulation Modes

Select one primary mode and combine modes only when that improves the user's objective.

### Quick

Use for a lightweight consequence scan. Focus on the few most important downstream effects, dependencies, risks, and decision implications.

### Systems

Use for interacting technical or organizational components. Emphasize dependencies, bottlenecks, cascading failures, reversibility, operational burden, and observability.

### Stakeholder

Use when different actors have materially different incentives, knowledge, authority, or risk tolerance. Model behavior from those constraints rather than generating generic persona dialogue.

Actors must not know information they would not realistically possess.

### Adversarial

Use to search for ways a design, process, argument, or plan can fail. Potential adversarial forces include attackers, negligent operators, skeptical reviewers, malicious insiders, budget pressure, unexpected edge cases, or hostile environmental conditions.

### Decision Branch

Use when alternatives should be compared across materially different futures. Include a status-quo or do-nothing branch when it is genuinely informative.

### Temporal

Advance a system across an explicit horizon so maintenance burden, accumulated drift, delayed effects, adaptation, or path dependence can emerge.

### Chaos

Use when the explicit objective is resilience testing. Introduce one or more declared failure conditions such as dependency loss, stale data, expired credentials, broken integrations, reduced staffing, contradictory state, or degraded service.

Low-frequency high-impact conditions must be labeled as stress scenarios, not likely outcomes.

### Counterfactual

Change one meaningful condition and compare the resulting system with the observed or baseline state.

### Quantitative

Use only when numerical variables and defensible inputs exist. Prefer actual computation when available.

Do not invent precise probabilities or probability distributions merely because numbers would make the output look rigorous. If defensible distributions are unavailable, use qualitative branches instead.

## Procedure

### 1. Frame the question

Identify:

- what is being simulated;
- what the user wants to learn;
- scope and time horizon;
- the smallest useful granularity;
- the primary simulation mode;
- whether the user wants one likely path, several branches, or a stress test.

Prefer useful defaults over unnecessary clarification.

### 2. Ground the initial state

Determine which claims are already known and which require retrieval.

Retrieve external or connected evidence when the scenario materially depends on current or private state and the runtime permits it. Do not retrieve data merely to decorate a conceptual simulation.

Record material unknowns rather than filling them with invented certainty.

### 3. Declare assumptions and constraints

Surface only assumptions that could materially change the result.

If multiple plausible assumptions would produce different outcomes, branch rather than forcing one assumption into the baseline.

### 4. Instantiate actors and environment

Create only actors that causally matter.

For each important actor, model some subset of:

- objective;
- incentives;
- capabilities;
- available information;
- authority;
- constraints;
- risk tolerance;
- relationships.

Treat technical systems as actors only when their state transitions or automated behavior materially affect the scenario.

### 5. Establish baseline world state

Represent the current relevant condition before advancing time.

Track only state variables that influence later consequences, such as:

- service or component health;
- access or control;
- resource availability;
- workload;
- confidence or information quality;
- risk exposure;
- unresolved dependencies;
- narrative or strategic position.

### 6. Advance the world

Move the scenario through meaningful events and actor decisions.

For each step:

1. apply the event or decision;
2. update relevant state;
3. propagate first-order consequences;
4. inspect second- and third-order consequences where they materially matter;
5. identify feedback loops, bottlenecks, or new dependencies;
6. note warning signals an observer could realistically detect.

Do not simulate every moment. Use the coarsest time step that preserves the important causal structure.

### 7. Branch when necessary

Create alternate branches when:

- the user supplied alternatives;
- a decision point materially changes the trajectory;
- a key assumption is uncertain;
- the preferred solution needs a meaningful competitor;
- a do-nothing branch provides a useful baseline.

Prune branches that no longer change the decision.

### 8. Challenge the preferred outcome

For substantial decisions, perform at least one anti-confirmation check:

- **Inversion:** assume the preferred solution is wrong and identify why.
- **Competitor:** model a materially different alternative.
- **Status quo:** model what happens if nothing changes.
- **Failure search:** identify evidence that would invalidate the preferred conclusion.
- **Unknown-unknown scan:** ask what dependency or actor is absent from the model.

Do not manufacture false balance when one option is strongly supported by evidence.

### 9. Evaluate outcomes

Compare resulting states against the user's objective and any success/failure criteria.

Separate:

- robust findings that survive several plausible branches;
- fragile findings that depend heavily on assumptions;
- leading indicators that could be monitored in reality;
- reversible mitigations;
- high-cost or irreversible interventions.

### 10. Distill the result

Return the shortest report that preserves the important causal story.

The report should answer:

- What happened?
- Why did it happen?
- What surprised us?
- What would reveal this developing in reality?
- Which assumptions matter most?
- What should change before acting?

### 11. Preserve simulation boundaries

Do not persist hypothetical events as historical facts.

If the runtime supports durable knowledge routing, promote only durable findings such as validated requirements, architecture risks, runbook improvements, hypotheses, decisions, or eval cases. Raw imaginary timelines remain ephemeral unless the user explicitly asks to save them as scenarios.

## Output Contract

Use this structure for substantial simulations. Compress or omit empty sections for quick simulations.

```markdown
# Simulation Result

## Scenario
What was tested and over what horizon.

## Ground Truth
Important facts used to establish the starting state.

## Assumptions & Unknowns
Conditions introduced by the model and unresolved information that could change the result.

## What Happened
A concise causal progression or branch comparison.

## Emergent Effects
Consequences that arose from interactions rather than being explicitly supplied.

## Failure Modes
What broke, nearly broke, or became fragile.

## Decision Points
Moments where a different choice materially changes the trajectory.

## Leading Indicators
Observable signals that would reveal the scenario developing in reality.

## Robust Conclusions
Findings that survive multiple plausible assumptions or branches.

## Fragile Conclusions
Findings heavily dependent on uncertain assumptions.

## Recommended Actions
Practical changes justified by the exercise, favoring reversible steps when possible.

## Confidence
Confidence level and the uncertainties that dominate it.

## Durable Candidates
Findings worth preserving outside the simulation, if any.
```

For decision branches, a compact comparison table may precede the narrative when useful.

## Guardrails

- Simulation is not prediction.
- Never present invented scenario events as observed history.
- Never present simulated stakeholder behavior as knowledge of a real person's private thoughts or intentions.
- Keep FACT, ASSUMPTION, INFERENCE, HYPOTHETICAL, and UNKNOWN conceptually distinct.
- Do not fabricate citations, telemetry, probabilities, measurements, model outputs, or tool results.
- Do not invent numerical precision when the evidence supports only qualitative reasoning.
- Do not claim authoritative domain verification without the relevant authoritative tool or trusted source.
- A simulated action never constitutes authorization for a real action.
- Respect the active runtime's data-classification, privacy, permissions, and action-approval boundaries.
- Prefer reversible recommendations when uncertainty is high.
- Keep exploratory timelines ephemeral by default.
- Preserve disagreements or competing incentives until synthesis rather than prematurely averaging them away.

## Failure Handling

### Missing inputs

Proceed with explicit, minimal assumptions when the simulation can still answer the user's underlying question.

### Unavailable dependency

Continue with a qualitative or partially grounded simulation and state which evidence or verification is missing.

### Conflicting evidence

Surface the contradiction. If the conflict materially changes the result, simulate both interpretations.

### Excessive scope

Reduce granularity while preserving the important causal structure. For example, simulate representative weeks rather than every hour of a year.

### Unbounded branching

Retain only branches that materially affect the user's objective.

### Unsupported probability request

Decline to manufacture percentages. Provide qualitative likelihood, sensitivity analysis, or explicit scenarios instead.

### Classification mismatch

Do not move restricted invocation data into a less-trusted durable home. Continue ephemerally when permitted.

### Stale canonical source

Mark the relevant starting state as uncertain or retrieve a fresher authoritative source when available.

## Examples

### Technical system

```text
Simulate rollout of this Conditional Access policy for 30 days. Focus on operational failure modes and what the help desk would see first.
```

### Decision branches

```text
Run three futures from this decision: adopt the new architecture now, defer six months, or keep the current design. Compare reversibility, operating burden, and long-term risk.
```

### Adversarial

```text
Stress-test this design. Assume a capable but realistic adversary is trying to exploit the weakest dependency.
```

### Narrative

```text
Simulate the consequences if this character tells the truth halfway through the story. Preserve established characterization and world rules.
```

### Strategy

```text
From this position, simulate three strategic plans rather than only choosing a move. Clearly distinguish human-style strategic reasoning from engine verification.
```

## Registration Checklist

1. Save as `skills/simulation-lab/SKILL.md`.
2. Register as `skill.reasoning.simulation-lab` in `catalog.yml`.
3. Keep the canonical body public and model-neutral.
4. Add stable natural-language aliases.
5. Run `python scripts/validate_catalog.py`.
6. Review the diff for private, employer-confidential, or secret material.
