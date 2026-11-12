# Sources, inclusion criteria, and publication boundaries

## Source material

1. **`Project3 Instructions.zip`** (shared in chat): MIT-licensed RC-DS Project 3 starter code; only HEAL-relevant Python files copied into `starter/heal/` with one machine-specific default path redacted. The original LICENSE is retained.
2. **Task 3 Notion export** (shared in chat): summarized in `docs/project-scope.md`. The original page and image are not redistributed.
3. **Lab robot-PC source snapshot** (shared in chat): statically inspected to derive architecture, safety issues, command interfaces and outstanding questions. Proprietary vendor source, binaries, raw machine settings and logs are **not published**.
4. **Earlier HEAL analysis documents** (generated from archive): used to draft the concise documentation here, while avoiding wholesale publication of internal inventories and machine-specific information.

## Explicit exclusions

- `/addverb/cobot_backend` vendor headers and proprietary libraries
- Older full `Debojit_WS`, `bimanual_ws`, generated `build`/`install`/`log` trees
- Real deployment credentials and the plaintext SSH password in the starter README
- Internal machine addresses, private host/user paths in the README, personal tokens and keys
- Franka-only and unrelated bimanual code
- Raw robot motion traces and experimental logs not directly needed for this assignment

The source examples themselves may contain lab-specific filesystem defaults, which should be reviewed before adapting them to a new machine. Reproduction requires authorized access to the separately provisioned vendor driver and hardware environment.
