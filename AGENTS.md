# Agents.md – Codex Agent Build Instructions

## Goal

Automate the generation, validation, and documentation of AI Agents’ source code while ensuring quality and preventing infinite re‑tries.

## High‑Level Loop

1. **Generate / Modify Code**
   • Use the current prompt and context to produce the necessary code changes.
2. **Self‑Review**
   • Diff the working tree; comment inline on risky or untested sections.
   • **Run linting / formatter checks** (e.g., `ruff`, `black`, `eslint`, `prettier`) and fail the step on any violations.
   • Ensure style, security, and dependency hygiene rules are respected.
3. **Run Full Test Suite** (`pytest -q` or project‑specific runner).
4. **Decision Gate**
   • **Pass:** proceed to Step 5.
   • **Fail:** rewrite the prompt or adjust the code, commit, and **repeat Steps 2‑4**.
   – Increment `ATTEMPT_COUNT`.
   – **Abort after 5 failed attempts** and flag human review.
5. **Documentation Update**
   • Regenerate or patch all markdown docs, docstrings, and change‑logs so they reflect the final codebase.
   • Push docs with the same commit that turns the CI green.

## Control Variables

| Name            | Default | Purpose                            |
| --------------- | ------- | ---------------------------------- |
| `ATTEMPT_COUNT` | 0       | Tracks the current retry number.   |
| `ATTEMPT_LIMIT` | 5       | Hard cap to prevent endless loops. |

## Pseudocode Skeleton

```pseudo
while ATTEMPT_COUNT < ATTEMPT_LIMIT:
    generate_or_modify_code()
    self_review_changes()
    result = run_tests()
    if result.success:
        update_documentation()
        exit 0
    else:
        refine_prompt()
        ATTEMPT_COUNT += 1

raise BuildError("Exceeded retry limit – manual intervention required")
```

## Best Practices for Prompt Refinement

* Isolate the failing unit first; regenerate only the minimal scope.
* Incorporate test error output directly in the new prompt.
* Preserve working code to avoid regression.

## Logging

* Record each attempt (number, diff summary, test outcome) to `codex_build.log` for auditing.
* Tag the successful build commit with `codex-agent:<version>`.

## Security & Compliance

* Never commit secrets or personal data.
* Enforce dependency pinning (`requirements.txt`, `package-lock.json`).
* Run static‑analysis hooks (`ruff`, `bandit`, etc.) during Self‑Review.

---

**End of file**
