# Grimoire Financial Narrative Update

## Purpose

Update a private longitudinal financial narrative from current finance data and authorized contextual interpretation rules while preserving provenance, uncertainty, and the distinction between transactions, household transfers, debt movement, and genuine spending.

## Use When

Use this skill for a monthly Financial Narrative Ledger update, a new baseline, or an evidence-backed review of longer-term financial patterns.

## Do Not Use When

Do not use it for the lightweight weekly spending snapshot, tax advice, investment execution, credit decisions, or unsupported judgments about motives.

## Inputs

- **Current finance data** — balances, accounts, categorized transactions, liabilities, assets, and reporting period.
- **Canonical ledger** — previous baselines, narrative entries, and current longitudinal interpretation.
- **Private interpretation rules** — user-confirmed mappings for transfers, shared household support, unlinked accounts, reimbursements, and known category corrections.
- **Comparison windows** — prior months or another explicitly chosen baseline.

## Dependencies

- Authorized access to current financial data and the private ledger.
- A private configuration source for interpretation rules and canonical selectors.
- Reliable timestamps and account identity sufficient to avoid double counting.

## Classification

The reusable method is **Public**. Account data, transactions, balances, debts, household relationships, interpretation rules, and ledger entries are **Personal Private**.

## Procedure

### 1. Load current authority

Fetch the latest available finance data, the existing narrative ledger, the previous comparable baseline, and current user-confirmed interpretation rules. Do not rely on a remembered rule when a newer canonical rule exists.

### 2. Normalize without erasing provenance

Separate spending, income, transfers, debt payments, reimbursements, shared-household support, and uncategorized activity. Preserve the original transaction source and any uncertainty attached to reclassification.

### 3. Build the new baseline

Record the period, account coverage, assets, liabilities, net worth, major spending categories, cash-flow context, known exclusions, and data freshness. Distinguish observed values from estimates.

### 4. Compare longitudinally

Identify material changes from prior months and emerging patterns that persist across more than one period. Separate structural movement from one-time events, partial-month effects, transfer noise, and data-coverage changes.

### 5. Update the narrative

Append or reconcile one dated baseline and concise interpretation. Preserve previous baselines as historical evidence. Revise a standing interpretation rule only when the user confirms the new rule or the canonical source explicitly changed.

### 6. Verify and report

Re-fetch the ledger and report the new baseline, material changes, emerging patterns, confidence limits, and unresolved classification questions.

## Output Contract

~~~markdown
# Financial Narrative Update

## Coverage
- Period:
- Accounts included:
- Known exclusions:
- Data freshness:

## Baseline
- Assets:
- Liabilities:
- Net worth:
- Cash-flow context:
- Major categories:

## Change Over Time
- Material changes:
- Emerging patterns:
- One-time effects:

## Interpretation
- Rules applied:
- Uncertainty:
- Questions requiring confirmation:

## Durable Result
- Ledger updated:
- Prior history preserved:
~~~

## Guardrails

- Never publish personal financial data or household interpretation rules.
- Never count transfers as spending without evidence.
- Never infer hidden accounts, motives, or obligations.
- Never present incomplete data as a complete financial picture.
- Never give high-stakes financial advice as certainty; separate observation from optional guidance.

## Failure Handling

- **Data unavailable or stale:** report the limitation and do not manufacture a baseline.
- **Coverage changed:** annotate the comparability break.
- **Ambiguous transaction:** preserve uncertainty and request confirmation instead of forcing a category.
- **Ledger write unavailable:** return a ready-to-apply baseline and state that no durable update occurred.

## Example

~~~text
/skill financial-narrative-update
Add a new monthly baseline using my current finance data and private interpretation rules.
~~~
