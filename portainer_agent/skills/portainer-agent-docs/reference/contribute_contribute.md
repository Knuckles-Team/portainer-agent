We value contributions from the Portainer community and encourage developers to propose fixes, improvements, and new ideas.
The following guidelines outline our engineering workflows, please review these before making a contribution to ensure any changes can be integrated smoothly.
##
[hashtag](https://docs.portainer.io/contribute/contribute#contributing-to-the-portainer-ce-codebase)
Contributing to the Portainer CE codebase
The Portainer CE codebase is available in [build instructions](https://docs.portainer.io/contribute/build) and the following guidelines when making a contribution.
###
[hashtag](https://docs.portainer.io/contribute/contribute#repository-structure)
Repository structure
  * Our main development occurs in private repositories, which are mirrored to public GitHub repos (e.g.
  * The `develop` and `release/*` branches in public repositories are **read-only** : merges into these branches are blocked to preserve synchronization with our internal repositories.
  * We maintain a separate `community` branch in each public repository to accept and review external contributions.


###
[hashtag](https://docs.portainer.io/contribute/contribute#contribution-process)
Contribution process
  1. **Fork the repository**
     * Create your own fork of the relevant Portainer public repository.
  2. **Create a feature branch**
     * Base your changes on the current `develop` branch (not `main`, `release/*`, or `community`). This ensures you are working off the latest version of the codebase.
  3. **Submit a Pull Request (PR)**
     * Open your PR against the `develop` branch.
     * Portainer engineers will update the target branch to `community` when the contribution is ready to be merged.
  4. **Review and feedback**
     * Contributions will be reviewed by Portainer engineers.
     * We may request changes to align with coding standards, tests, or design decisions.
     * In some cases, we may adapt or refactor a contribution before merging.
  5. **Integration**
     * Once approved and merged into `community`, Portainer engineers will cherry-pick contributions into the upstream private repository.
     * These changes will then flow into `develop` and subsequent releases through our normal sync process.
     * Not all contributions will be integrated upstream. Decisions will be based on roadmap alignment, technical fit, and quality.


###
[hashtag](https://docs.portainer.io/contribute/contribute#contribution-expectations)
Contribution expectations
  * **Coding standards** : Please follow existing project style and conventions.
  * **Tests** : Include tests where applicable. Contributions without tests may be delayed.
  * **Documentation** : Update relevant docs (e.g. README, usage notes) when changing functionality.
  * **Scope** : Focus on well-defined features, fixes, or improvements. Large architectural changes should be discussed in an issue first.


circle-exclamation
###
[hashtag](https://docs.portainer.io/contribute/contribute#id-987d7792-f717-4a29-9fe7-b9014d343629)
AI assistance notice
If you use any form of AI assistance to create your contribution - whether for code, documentation, or drafting pull request (PR) responses - it must be disclosed in your pull request description.
Trivial assistance, like single-word auto-completion, does not require disclosure. Disclosing AI usage helps maintainers apply the correct level of scrutiny during review.
For commits where an AI tool has significantly contributed to the code, it is recommended to add a Co-Authored-By trailer in the commit message to formally credit the tool, using the format specified by the tool's provider.
###
[hashtag](https://docs.portainer.io/contribute/contribute#communication)
Communication
  * For significant changes or new features, use
  * PR discussions are the best place for clarifications on specific contributions.


##
[hashtag](https://docs.portainer.io/contribute/contribute#reporting-bugs)
Reporting bugs
If you find a bug,
[This article](https://docs.portainer.io/faqs/contributing/how-do-you-decide-which-bugs-and-features-to-work-on-first) covers how we prioritize bug fixes.
##
[hashtag](https://docs.portainer.io/contribute/contribute#feature-requests)
Feature requests
You can request new features by posting an Idea in our
Learn how we prioritize feature development [in this article](https://docs.portainer.io/faqs/contributing/how-do-you-decide-which-bugs-and-features-to-work-on-first).
[PreviousAPI usage exampleschevron-left](https://docs.portainer.io/api/examples)[NextBuild instructionschevron-right](https://docs.portainer.io/contribute/build)
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.portainer.io/privacy-policy).
close
AcceptReject
