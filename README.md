# Paperclip Docs Skill

`paperclip-docs` is a portable Agent Skill that helps AI coding agents work with Paperclip using current official documentation, the installed `paperclipai` CLI, live REST API behavior, and the `paperclipai/paperclip` source repository.

## What it does

The skill provides source-backed guidance for:

- installation, onboarding, configuration, authentication, and deployment;
- context profiles, companies, agents, org charts, goals, projects, and issues;
- heartbeats, runs, approvals, budgets, costs, workspaces, and adapters;
- skills, routines, plugins, secrets, and storage;
- CLI/API usage, troubleshooting, security, upgrades, and migrations;
- architecture, source-code questions, and platform development.

It makes the agent verify the active context, instance, permissions, and installed CLI contract before suggesting changes. It defaults to read-only diagnosis and protects credentials and company data.

## Relationship to Paperclip's coordination skill

Use `paperclip-docs` for product knowledge, setup, administration, integration, debugging, and platform development. Paperclip also ships an official `paperclip` coordination skill for agents operating inside a heartbeat to manage assignments, issue status, delegation, comments, and company governance. The two skills serve different purposes and can be installed together.

## Install

Use the open Agent Skills CLI for Codex, Claude Code, Cursor, and many other supported agents:

```bash
npx skills add art12slavik/paperclip-docs
```

Install globally for the current user:

```bash
npx skills add art12slavik/paperclip-docs --global
```

To target a particular supported agent, add `--agent <agent-id>`.

### Manual installation

Clone the repository to a stable location:

```bash
git clone https://github.com/art12slavik/paperclip-docs.git /path/to/paperclip-docs
```

Copy or symlink the entire `paperclip-docs` directory into your agent's skills directory so it can discover `SKILL.md`. Consult your agent's documentation for its project-level or global skills path.

Alternatively, reference the skill directly:

```text
Use $paperclip-docs at /path/to/paperclip-docs to configure or troubleshoot Paperclip using current official sources.
```

## Requirements and compatibility

- Any agent that supports the common `SKILL.md` Agent Skills format.
- Web, repository, installed CLI, or authorized read-only API access is recommended for accurate environment-specific guidance.
- Python 3 is optional and only needed for `scripts/fetch_paperclip_docs.py` when no native documentation fetcher is available.
- `agents/openai.yaml` is optional metadata for compatible OpenAI clients.

## Included files

- `SKILL.md` — core agent instructions and safety boundaries.
- `references/source-map.md` — routing to authoritative Paperclip sources.
- `references/playbooks.md` — troubleshooting, configuration, mutation, upgrade, and development workflows.
- `scripts/fetch_paperclip_docs.py` — restricted helper for fetching official documentation and repository files.

## Official sources

- [Paperclip documentation](https://docs.paperclip.ing/)
- [Paperclip repository](https://github.com/paperclipai/paperclip)

This is an independent helper skill and is not an official Paperclip project.
