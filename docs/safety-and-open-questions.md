# Safety review and unresolved checks

**Status:** Findings are from static inspection of the user-provided starter and archived ROS source. They are not proof of currently deployed protection, compliance, or robot behavior.

## Before any robot movement

- Have the lab lead demonstrate the approved startup and emergency-stop/recovery sequence, verify reachable E-stop and exclusion area, and require a supervising second person.
- Confirm actual payload mass, tool shape, collision geometry, gripper type, workspace and per-joint range/speed limits.
- Determine the manufacturer meaning of `safety_type: 1.0`, which maps to `eNoHumanSafety` in one code enumeration. **Do not infer whether human-collaboration protections are enabled.**
- Verify active controller state and whether the optional safety relay is running, gating commands, and monitoring stale/invalid feedback.
- Never use the sample scripts as direct live-hardware instructions; require low-speed testing, simulation first, and a written risk assessment.

## Source-level concerns

1. Some example ROS nodes write directly to `/velocity_controller/commands`. The optional velocity relay is not automatically launched by the standard velocity-control launch file.
2. The velocity controller and joint-jogging handlers assume six command elements in code paths reviewed; malformed command validation deserves review.
3. Controller-side stale-command behavior was not established from the exported code. An application sending no messages is not sufficient proof that motion safely stops.
4. Joint limit ranges differ between the URDF and separate utility/relay settings for all six joints. Reconcile against manufacturer specifications and the actual robot configuration.
5. The gripper service sets success in a case where an invalid request is rejected; check service responses rather than trusting only the success bit.
6. DLS example lacks a universally enforced joint-limit guard and output slew limiting is optional and off by default in the starter implementation.
7. A legacy recorder computes a sampling interval using an integer-second conversion; the timing of high-frequency recordings needs independent validation.
8. Some example scripts do not reject stale or incomplete joint feedback; avoid substituting zeros for unknown joint states.
9. Starting a ROS hardware interface may call robot power-on during activation.

## Open questions for the lab

- Which machine-side HEAL server build and ROS workspace were used successfully most recently?
- What is the exact procedure for gravity compensation/free drive, and which controller must be active or inactive?
- What hardware watchdogs, safety-rated stop functions, collision detection, and fault recovery are installed?
- Which gripper/probe is currently mounted, and are its TCP, payload and calibration known?
- Can the wire contact circuit publish timestamped events without adding unsafe electrical coupling?
- Are force/torque messages from the vendor wrapper, external sensor, or remapped topic?

No project script should command motion before these are answered and reviewed.
