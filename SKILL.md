---
name: paperclip-docs
description: Provide current, source-backed guidance for Paperclip from its official documentation, installed paperclipai CLI, live REST API behavior, and paperclipai/paperclip repository. Use for Paperclip installation, onboarding, configuration, deployment, authentication, context profiles, companies, agents, org charts, goals, projects, issues, heartbeats and runs, approvals, budgets and costs, workspaces, adapters, skills, routines, plugins, secrets, storage, CLI/API usage, troubleshooting, security, architecture, source-code questions, and implementation or migration work that depends on accurate Paperclip behavior.
---

# Paperclip Docs

Give accurate Paperclip guidance and make narrow, auditable changes. Prefer evidence from the user's installed CLI, active instance, and matching repository revision when these can differ from current public documentation.

## Keep this skill distinct

- Use this skill for Paperclip product knowledge, setup, administration, integration, debugging, API/CLI work, and platform development.
- Use Paperclip's official `paperclip` coordination skill instead when an agent is inside a heartbeat and needs to check assignments, update issue status, delegate, comment, or follow company governance.
- Do not use Paperclip merely because the user's actual domain work happens to be tracked there.

## Work portably

- Use whatever read-only capabilities the host agent provides: web search/fetch, a browser, repository search, file reads, shell commands, or an authorized Paperclip client.
- Do not depend on Codex-specific, Claude-specific, or Paperclip-specific tool names.
- If web access exists, use the official sources below. If only a shell is available, optionally run `python {baseDir}/scripts/fetch_paperclip_docs.py`.
- If neither the web nor a current local checkout is available, answer from available local evidence and label it as potentially stale.

## Classify the request

Choose the smallest applicable workflow:

1. **Explain or answer** — retrieve the exact official page and answer with a direct link.
2. **Diagnose** — inspect CLI help, active context, configuration health, and read-only API/status evidence; explain the cause before changing anything.
3. **Configure or implement** — inspect current settings, persona, company scope, and exact command/API contract before applying a narrow change.
4. **Operate the control plane** — distinguish board authority from agent authority and treat every company-scoped mutation as consequential external state.
5. **Develop Paperclip itself** — use the checked-out repository's `AGENTS.md`, local docs, source, tests, package scripts, and default `master` branch conventions at that revision.
6. **Compare versions or discuss releases** — use official releases, tags, package versions, and commit history; state the versions compared.

## Route sources

Use sources in this order, stopping when the claim is established:

1. **Installed and live-instance truth**
   - Use `paperclipai --help` and `paperclipai <command> --help` for the installed command surface.
   - Use `paperclipai context show` to identify API base, profile, persona, default company, and credential env-var name without printing the token itself.
   - Use `paperclipai doctor` for read-only instance checks. Do not add `--repair` or `--fix` during diagnosis.
   - Use `GET /api/health` and narrowly scoped read endpoints when live behavior matters.
2. **Official documentation**
   - Search within `https://docs.paperclip.ing/` and fetch the exact guide or CLI/API reference page.
   - Use the repository's `docs/docs.json` and `docs/` tree as the machine-readable documentation map when helpful.
3. **Official source**
   - Use `https://github.com/paperclipai/paperclip` for implementation details, repository instructions, release artifacts, and docs source.
   - Prefer a tag matching the installed package/server version; otherwise say that `master` may be newer.
4. **Issues and discussions**
   - Use official-repository issues or discussions only for unresolved bugs or maintainer context. Label workarounds as provisional unless documented or merged.

Read [source-map.md](references/source-map.md) for topic routes. Read [playbooks.md](references/playbooks.md) before configuration changes, troubleshooting, deployments, control-plane mutations, upgrades, or repository work.

## Answer from documentation

1. Reduce the question to two to six search terms.
2. Select the narrowest live docs page; do not rely on the docs landing page or a search excerpt alone.
3. Read the matching CLI/API page and, when necessary, the `docs/` Markdown or implementation at the relevant tag.
4. Cross-check installed CLI help, selected context/profile, or live API response when behavior can vary by version or persona.
5. Lead with the answer. Include exact commands, flags, JSON fields, routes, and state transitions only when supported.
6. Link directly to each official page or repository file used. Distinguish documented fact, local verification, source-code inference, and uncertainty.

## Preserve Paperclip boundaries

- Distinguish setup commands from control-plane commands. Setup operates on local instance files/processes; the control plane calls a server and requires credentials.
- Do not confuse bare `paperclipai run`, which bootstraps/starts a local server and may repair by default, with `paperclipai run <subcommand>`, which manages heartbeat runs through the API.
- Resolve company scope explicitly. The CLI may obtain it from `--company-id`, `PAPERCLIP_COMPANY_ID`, or the selected profile.
- Respect persona and tenant boundaries. A board profile has broad instance authority; an agent profile is scoped to its company and agent identity.
- During a Paperclip heartbeat, include the current run audit header on mutations as required by the official coordination skill.
- Treat HTTP `409` checkout conflicts as ownership conflicts, not transient errors to retry blindly.

## Change configuration safely

1. Identify the CLI/server version, data directory or instance, config path, deployment mode/exposure, API base, context profile, persona, and company scope.
2. Inspect current values with read-only commands and exact official references before editing.
3. Preserve unrelated JSON/config, context profiles, database/storage settings, secrets, agent configs, skills, audit history, and company data.
4. Prefer a dedicated `paperclipai configure --section ...`, context command, or narrowly scoped API/CLI mutation over replacing whole files or records.
5. Validate local configuration with `paperclipai doctor`. Use `--repair` only when explicitly authorized after reviewing the proposed repairs.
6. Re-run the smallest health check or read endpoint and report the resulting state and audit impact.

Never reveal API keys, board tokens, agent JWT secrets, provider credentials, secret values, local master keys, invite tokens, session cookies, or webhook secrets. Prefer credential environment-variable references in context profiles instead of plaintext tokens.

## Handle mutations and security

- Treat onboarding, server start/stop, repair, configuration writes, company creation/deletion/archive/import, agent hire/pause/resume/terminate, issue checkout/update, approval decisions, run cancellation, budget changes, skill/plugin installs, secret operations, and routine changes as state-changing operations.
- Preview the exact instance, profile, persona, company, entity ID, and expected impact before consequential changes. Obtain user approval when the surrounding agent policy requires it.
- Prefer backups, exports, config revisions, dry runs, archives, and reversible actions where supported.
- Do not weaken authentication, exposure settings, allowed hostnames, company isolation, permissions, approval gates, budget enforcement, sandboxing, plugin capabilities, or secret handling merely to make an error disappear.
- Treat third-party adapters, skills, plugins, packages, and install scripts as untrusted code. Inspect provenance and requested capabilities before enabling them.

## Keep guidance current

When the user asks for current, latest, supported, recommended, or secure behavior, retrieve live official sources during the task. Include the installed/client/server version and retrieval date when drift could matter. If live retrieval fails, say which fallback was used and that it may be stale.
