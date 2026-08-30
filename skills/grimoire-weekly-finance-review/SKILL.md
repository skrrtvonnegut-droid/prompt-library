# Grimoire Weekly Finance Review

## Purpose

Produce a concise current-state finance review covering month-to-date spending, net-worth movement, and practical next actions without confusing transfers, incomplete coverage, or partial-month timing with real financial change.

## Use When

Use this skill for a weekly finances update, a current spending snapshot, or a lightweight net-worth check.

## Do Not Use When

Do not use it for the longitudinal monthly narrative, tax advice, investment execution, lending decisions, or a complete financial plan.

## Inputs

- **Current finance data** — balances, liabilities, categorized transactions, income, and data freshness.
- **Comparison data** — the previous month and, when available, the same elapsed portion of that month.
- **Private interpretation rules** — confirmed handling of transfers, household support, reimbursements, debt payments, and unlinked accounts.

## Dependencies

- Authorized read access to current financial data.
- A private configuration source for category corrections and household interpretation.
- Sufficient account coverage to describe net worth and spending limits honestly.

## Classification

The reusable method is **Public**. Transactions, balances, debts, household mappings, and recommendations tailored to them are **Personal Private**.

## Procedure

### 1. Establish coverage

State the reporting date, included accounts, data freshness, and known exclusions. Apply only current user-confirmed interpretation rules.

### 2. Compare spending

Compare month-to-date categories with the prior month. Prefer same-days-elapsed comparison when possible, while retaining the completed prior month as context. Identify the categories driving the difference and distinguish one-time expenses from recurring movement.

### 3. Reconcile net worth

Calculate or retrieve assets, liabilities, and net worth from covered accounts. Explain material movement using observed balance changes without inventing causes.

### 4. Identify practical next actions

Offer a small number of actions proportional to the evidence. Prioritize data cleanup, bill or cash-flow awareness, category anomalies, debt tracking, or deliberate follow-up. Avoid generic austerity advice when the data does not support it.

### 5. Report uncertainty

Call out unlinked accounts, stale balances, ambiguous transactions, incomplete categories, and partial-month distortions.

## Output Contract

~~~markdown
# Weekly Finances Review

## Coverage
- As of:
- Included:
- Missing or stale:

## Month-to-Date Spending
- Category changes:
- Main drivers:
- One-time effects:

## Net Worth
- Assets:
- Liabilities:
- Net worth:
- Material movement:

## Suggested Next Actions
1.
2.
3.

## Uncertainty
- Classification or coverage limits:
~~~

## Guardrails

- Never expose private finance data outside the authorized response or destination.
- Never treat transfers or debt principal as ordinary consumption without evidence.
- Never infer motives or hidden obligations.
- Never present partial coverage as complete net worth.
- Keep guidance informational and proportionate to uncertainty.

## Failure Handling

- **Finance source unavailable:** return a blocked report rather than estimating.
- **Comparison period missing:** provide the current snapshot and label the comparison unavailable.
- **Ambiguous transaction:** preserve the ambiguity and ask for confirmation only when it materially changes the result.

## Example

~~~text
/skill weekly-finance-review
Give me the current weekly finances update from my authorized finance data.
~~~
