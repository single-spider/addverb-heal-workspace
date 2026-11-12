# Teaching and evaluation data

This public repository contains **schemas and validation only**, not raw robot data.

`teach_joint_states.csv` can use the header in `teach_joint_states.schema.csv`:

- `timestamp_sec`: absolute or monotonic seconds, consistent within one recording.
- `joint1` through `joint6`: joint positions in **radians**, ordered by explicitly verified joint names.

Optionally add velocity columns and an external separate timestamped event file for wire contact. Preserve the originating clock source, URDF/tool revision, controller version, and physical session metadata outside the CSV. Real robot logs belong in a lab-approved private data store.

The schema CSV has only a header. It is **not a demonstration trajectory**.
