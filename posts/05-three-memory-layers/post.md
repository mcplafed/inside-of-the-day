# Graphiti vs Graphify vs Cognee? I use them all. Here's why.

## Core insight

Graphiti, Graphify, and Cognee can look like competing answers to the same "agent memory" problem. I use all three because my agents ask three different kinds of questions.

## Mechanism

Three complementary layers, each answering a distinct kind of question:

- **Graphiti** (https://github.com/getzep/graphiti) - temporal memory. Builds temporal context graphs: it tracks facts and relationships over time, preserves provenance back to episodes, supports incremental updates, and lets an agent query what is true now or what was true before. Question it answers: *what happened, changed, or was decided?* Examples: decisions, incidents, preferences, historical facts.
- **Cognee** (https://github.com/topoteretes/cognee) - document knowledge. Ingests documents and data into persistent agent memory, combining vector retrieval with graph relationships. In my system it is the document knowledge / RAG layer, isolated by datasets, for runbooks, architecture docs, policies, and guidance. Question it answers: *what do the documents say?*
- **Graphify** (https://github.com/Graphify-Labs/graphify) - code structure. Maps code into a queryable structural graph. Extraction is local Tree-sitter AST, capturing calls, imports, inherits, and cross-file relationships, so it can answer path, neighbor, impact, and structure questions without treating code as flat document chunks. Question it answers: *how does this codebase actually work?*

## Why all three

In this architecture, none replaces the other two. Graphiti is not where I query callers. Graphify is not where I record why a policy changed last quarter. Cognee is not my timeline of superseded decisions. Different questions want different graphs.

## Agent workflow

A single practical loop:

1. **Recall decisions** in Graphiti (temporal memory) before acting.
2. **Retrieve docs** in Cognee within an explicit dataset.
3. **Trace code** paths and impact in Graphify from the locally built AST graph.
4. **Execute** the task.
5. **Update durable knowledge**: durable decisions and outcomes return to Graphiti; changed docs are reindexed in Cognee and changed code is rebuilt in Graphify, so each layer stays current in its own store.

## Takeaway

Graphiti remembers time. Cognee retrieves meaning. Graphify maps structure. One agent workflow, three graphs - none replaces the other two.

## Companion Medium article

This LinkedIn post is the standalone summary. Publish the Medium article first, then add its verified canonical URL to `caption.txt` before the three source links using this line:

`The full architecture, routing rules, and write-back loop: <MEDIUM_URL>`

## Sources

- Graphiti: https://github.com/getzep/graphiti
- Cognee: https://github.com/topoteretes/cognee
- Graphify: https://github.com/Graphify-Labs/graphify

## Assets

- `assets/infographic.png`: final LinkedIn visual, 3240x4050 px (1080x1350 logical canvas at 3x).
- `source/infographic.html`: editable, self-contained visual source (no external assets or network dependencies).
- `source/render.py`: deterministic Playwright/Chromium renderer (viewport 1080x1350, device scale factor 3).
