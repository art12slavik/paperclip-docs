# Official source map

Use this file to choose the narrowest official source. Do not load every page.

## Discovery

- Documentation home: <https://docs.paperclip.ing/>
- Official repository: <https://github.com/paperclipai/paperclip>
- Documentation source: <https://github.com/paperclipai/paperclip/tree/master/docs>
- Documentation navigation: <https://github.com/paperclipai/paperclip/blob/master/docs/docs.json>
- Repository releases: <https://github.com/paperclipai/paperclip/releases>
- Security policy: <https://github.com/paperclipai/paperclip/blob/master/SECURITY.md>
- Repository guidance: <https://github.com/paperclipai/paperclip/blob/master/AGENTS.md>

The live docs site has routes that may not map one-to-one to repository filenames. Use live pages for current user-facing guidance. Use `docs/docs.json`, repository search, and the `docs/` tree to locate clean Markdown or pin a revision; do not guess a raw path from a website URL.

## Topic routes

| Topic | Start here | Version/live check |
|---|---|---|
| Installation and onboarding | `https://docs.paperclip.ing/guides/getting-started/installation/` | installed help, data directory/instance, `paperclipai doctor` |
| CLI installation and local run | `https://docs.paperclip.ing/reference/cli/installation/` | `paperclipai onboard --help`, `paperclipai run --help` |
| CLI mental model | `https://docs.paperclip.ing/reference/cli/overview/` | active context and installed help |
| Setup commands | `https://docs.paperclip.ing/reference/cli/setup-commands/` | `paperclipai doctor`, config/data-dir selection |
| Common flags and scope | `https://docs.paperclip.ing/reference/cli/common-options/` | selected profile, env, company id resolution |
| Authentication and context | `https://docs.paperclip.ing/reference/cli/authentication/` | `paperclipai context show`, persona, credential source |
| Companies | `https://docs.paperclip.ing/reference/cli/company/` and `/reference/api/companies/` | caller persona, company id, server response |
| Agents and org chart | `https://docs.paperclip.ing/reference/cli/agent/` and `/reference/api/agents/` | permissions, config revision, adapter type |
| Goals and projects | `https://docs.paperclip.ing/reference/api/goals-and-projects/` plus CLI goal/project pages | company scope and live record state |
| Issues/tasks | find the CLI issue and API issues pages through docs search | assignee, checkout owner, status, blockers, run id |
| Heartbeats and runs | find CLI run and heartbeat pages through docs search | exact distinction between bare `run` and subcommands |
| Approvals and governance | find CLI/API approval pages through docs search | persona, permission, decision status, audit trail |
| Costs and budgets | find cost/budget pages through docs search | current spend, policy and hard-stop state |
| Adapters | `https://github.com/paperclipai/paperclip/blob/master/docs/adapters/overview.md` | installed adapter/plugin version and environment probe |
| Skills | agent-developer writing/store guides and CLI skills reference | target agent/tool, install provenance, policy scan |
| Routines | CLI routine/reference pages | company, trigger, concurrency, assigned agent |
| Plugins | CLI plugin page and repository plugin spec | host compatibility, capabilities, worker status |
| Secrets | `https://docs.paperclip.ing/reference/cli/secrets/` and `/reference/deploy/secrets/` | provider health, references only; never print values |
| Deployment | find deployment mode, database, storage, environment, and exposure pages | live config, health, proxy/TLS, non-root runtime |
| REST API | `https://docs.paperclip.ing/reference/api/overview/` | live response, auth actor, exact company scope |
| Troubleshooting | installation troubleshooting plus setup commands | `paperclipai doctor`, resolved API base, logs |
| Product architecture | repository README, `doc/PRODUCT.md`, current docs architecture page | matching tag or commit |
| Repository development | root `AGENTS.md` and `doc/DEVELOPING.md` | checked-out commit and nested instructions |

## Source interpretation

- Treat installed CLI help and observed live-instance behavior as authoritative for that installation.
- Treat current docs as authoritative for current public contracts and workflows.
- Treat repository source at a matching tag as authoritative for implementation details of that release.
- Treat `master` as potentially newer than a deployed instance or installed npm package.
- Treat old `paperclipai/docs` repository content as archival; the current `paperclipai/paperclip` repository and live docs take priority.
- Treat issues, pull requests, and discussions as evidence of ongoing work, not released behavior, unless merged and present in the relevant release.
