# Template Method demo

This module demonstrates a minimal Template Method pattern in Python:

- `DeploymentSummary`: defines the fixed checklist for building a release summary.
- `EmailDeploymentSummary`: customizes the final formatting for email.
- `SlackDeploymentSummary`: customizes the final formatting for Slack.

## Run

```powershell
uv sync
uv run python -m app.main
```

## Test

```powershell
uv run pytest
```