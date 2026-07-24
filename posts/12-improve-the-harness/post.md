# Inside of the Day #12 - Do not bury a long agent session

## Core insight

A substantial agent session produces operational learning, not just a final answer. The reusable output is the set of durable, verified improvements it can make to the harness: memory, scoped operating rules, helper scripts, and skills.

## Mechanism

Install a native `/improve` command for the agent environment. At the end of a substantial session it reviews the work for repeated patterns, corrections, failed assumptions, and fragile commands. It then routes only evidence-based lessons to the smallest correct destination:

- durable decision or environment fact -> shared memory;
- scoped instruction -> applicable `CLAUDE.md` or `AGENTS.md`;
- repeated or fragile command -> tested helper script;
- reusable multi-step procedure -> update to an existing skill, or a new skill when distinct enough.

## Boundary

`/improve` is not transcript archival. It must not persist secrets, credentials, customer data, raw logs, temporary task state, or one-off details. It must avoid duplicate rules and make only small, verified changes.

## Practical prompt

```text
Create a reusable command called /improve for this agent environment.

First inspect how this system supports reusable commands, skills, prompts, or plugins. Use the simplest native mechanism that makes /improve available in future sessions.

When invoked at the end of substantial work, review the session for durable lessons, repeated mistakes, failed assumptions, unnecessary retries, and fragile or overly long shell commands. Turn only evidence-based lessons into the correct memory, scoped instructions, helper scripts, or existing skills. Never persist secrets, raw logs, private data, or temporary task state. Validate every change and report what changed, why, where it was saved, and what was deliberately not persisted.
```

## Claim scope

This is an operator practice and a proposed workflow, not a benchmarked claim about every agent system. The exact implementation differs by agent environment.

## Assets

- `caption.txt` - frozen LinkedIn caption
- `source/infographic.html` - editable 4:5 visual source
- `assets/infographic.png` - final 3240x4050 PNG
- `assets/mobile-probe.png` - 400x500 feed-size probe
