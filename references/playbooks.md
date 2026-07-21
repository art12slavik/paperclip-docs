# Paperclip playbooks

## Contents

- [Read-only troubleshooting](#read-only-troubleshooting)
- [Configuration change](#configuration-change)
- [Control-plane mutation](#control-plane-mutation)
- [Upgrade or migration](#upgrade-or-migration)
- [Repository development](#repository-development)
- [Source-backed response](#source-backed-response)

## Read-only troubleshooting

Start with commands that do not write or start services:

```bash
paperclipai --help
paperclipai context show
paperclipai doctor
paperclipai env
```

Then inspect the resolved API base and request `GET /api/health`. Use `paperclipai <command> --help` before relying on a flag that may differ by version.

Safety notes:

- Do not run bare `paperclipai run` merely to diagnose; it starts a local instance and repair is enabled by default.
- Do not add `doctor --repair`, `doctor --fix`, or `--yes` during read-only diagnosis.
- `paperclipai env` can describe secret-bearing variables. Do not paste its export block into chat or logs; report only set/default/missing state with values redacted.

Interpret the first failure:

1. CLI missing or wrong package/version → inspect Node/pnpm/npm setup and executable resolution.
2. Doctor fails before server start → inspect the selected config/data directory, deployment/auth compatibility, JWT secret presence, secrets/storage/database/provider checks, log directory, and port.
3. Health endpoint unreachable → inspect resolved API base, server process, bind/exposure, proxy, allowed hostnames, and logs.
4. `401` → credential missing/invalid or wrong profile; inspect credential source without printing it.
5. `403` → persona, permission, membership, or company boundary; do not retry with broader credentials automatically.
6. `404` → wrong ID, wrong company, wrong API base, or unavailable route/version.
7. `409` → checkout/ownership conflict; do not retry blindly.
8. Agent run fails → inspect adapter environment probe, workspace, heartbeat/run log, budget/approval gates, and config revision.

## Configuration change

1. Record installed CLI/server version, data directory/instance, config path, deployment mode/exposure, API base, active context profile, persona, and default company.
2. Read current config/context and the exact live docs or installed help for the target field.
3. Prepare a minimal change and identify affected instance, service, and company.
4. Prefer `paperclipai configure --section <section>` or a supported context/config command over direct whole-file replacement.
5. Apply only after change authorization is established.
6. Run `paperclipai doctor`, then repeat the relevant health/read check. Restart only when documentation requires it.

Never copy secret values into config examples or terminal output. Prefer `apiKeyEnvVarName` and Paperclip secret references.

## Control-plane mutation

Before a company, agent, goal, project, issue, approval, budget, run, routine, skill, plugin, or secret mutation:

1. Resolve API base, profile, persona, company, and exact entity ID.
2. Read the current entity and relevant permission/state-transition docs.
3. State the mutation, expected side effects, audit entry, and rollback/compensation path.
4. Use `--json` for structured automation and verify the returned entity.
5. During a heartbeat, include the required run audit header on mutations.
6. Re-read the entity and activity/audit record after the mutation.

Never substitute board credentials merely because an agent-scoped request returned `403`. Do not delete where archive/pause/revoke provides a safer reversible outcome.

## Upgrade or migration

1. Capture current client/server/package versions, installation method, config/data paths, deployment mode, database/storage/secrets providers, active plugins/adapters, and backup path.
2. Read target release notes and migration instructions across every skipped breaking boundary.
3. Back up database and configuration/secrets metadata using documented mechanisms; verify restore expectations.
4. Check Node/pnpm requirements, schema migrations, plugin compatibility, and public deployment variables before changing packages.
5. Upgrade only within authorized scope and never expose or migrate secrets implicitly.
6. Verify doctor, health, authentication, companies, adapters, heartbeat runs, approvals, budgets, plugins, and critical routines.

## Repository development

1. Read root `AGENTS.md` and any closer nested `AGENTS.md` before edits.
2. Inspect local `docs/`, `doc/`, source, `package.json`, workspace config, and lockfile at the checked-out commit before current web docs.
3. Use the repository's pnpm scripts and Node requirements; do not infer commands from unrelated projects.
4. Keep CLI/API behavior and documentation aligned when public contracts change.
5. Run the smallest relevant tests first. Follow repository guidance for broader typecheck, test, build, E2E, or release-smoke validation.
6. Cite file paths and commit/tag when explaining internal behavior.

## Source-backed response

Use this compact shape:

1. Direct answer or recommendation.
2. Exact supported command, JSON, or API route when needed.
3. Persona/company/version caveat or safety consequence when material.
4. Direct links to the specific official docs or repository files.

Clearly label:

- **Documented:** stated in official docs.
- **Verified locally/live:** observed from installed CLI, active context, health/API response, or source checkout.
- **Inferred from source:** reasoned from implementation rather than promised public behavior.
- **Uncertain:** official sources do not establish the claim.
