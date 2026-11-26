---
name: portainer-agent-docs
skill_type: skill
description: Portainer documentation and API reference pages for the portainer-agent connector. Use to answer questions about Portainer features, the EE API 2.39.0 endpoints, admin roles and registries by quoting the crawled pages. Do NOT use to operate a live environment (portainer-agent-operations).
crawl_depth: 2
source_url: https://docs.portainer.io, https://api-docs.portainer.io
categories: [Documentation, Knowledge Base, Reference]
tags: [docs, reference, portainer-agent-docs, knowledge-base]
---

# Portainer Agent Docs Documentation

Documentation and API references for Portainer agent

**Original Sources**:
- [https://docs.portainer.io](https://docs.portainer.io)
- [https://api-docs.portainer.io](https://api-docs.portainer.io)

**Contains**: 474 markdown files with full folder structure (crawled at depth 2).
*Last updated: March 05, 2026*

## 📚 Table of Contents

The full hierarchical table of contents (474 files) is in [references/contents.md](references/contents.md). The main groups are:

- `references/index/`: the Portainer EE API 2.39.0 reference pages and index.
- `references/versions_ee_2.39.0.yaml/`: the API specification split into numbered parts.
- Top-level pages: [Admin Registries Browse](references/admin_registries_browse.md), [Admin User Roles](references/admin_user_roles.md), [Contribute](references/contribute_contribute.md), [What's New](references/whats-new.md).

## Steps

1. Answer from the crawled pages. Start with `grep -ril "<keyword>" references/` to find the matching page. Verify at least one page matches before quoting.
2. Open the page with `cat references/<page>.md`, for example `references/admin_user_roles.md` for roles. Verify the passage you will quote is present.
3. For API questions, open the `references/index/PortainerEE-API-2.39.0.md` page. Verify the endpoint path and method you cite appear on it.
4. Quote the exact text and name the page file, for example `references/whats-new.md`, in the answer. Verify every claim maps to a quoted passage.

## Failure recovery

| Failure | Cause | Recovery |
|---------|-------|----------|
| No page matches | Keyword differs from the crawled wording | Search synonyms with `grep -ril`, or browse `references/contents.md` for the matching section. |
| Page content looks old | The crawl is dated (see "Last updated" above) | State the crawl date in the answer and, for live behavior, use `portainer-agent-operations` instead. |

## 🤖 Agent Usage Guide

- When the user asks anything about **Portainer Agent Docs**, consult the reference files.
- Prefer exact quotes and direct links to the relevant file/section.
- The hierarchical TOC above makes navigation fast and intuitive.
- All images and assets are preserved so links work perfectly.
