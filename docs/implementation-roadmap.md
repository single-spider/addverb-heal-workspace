# Wire-trace implementation roadmap

## Phase A: Read-only inventory and teaching data

1. Confirm names, units and order of six joints; collect URDF/tool geometry from an approved configuration.
2. Establish a method to capture `/joint_states` with original timestamps without commanding motion.
3. Log joint position, six velocities if present, time source, optionally EE pose, and contact signals. Reject missing/duplicate joints and stale messages.
4. Validate the CSV with `tools/validate_teach_csv.py` before processing.

## Phase B: Offline trajectory processing

1. Convert joint samples to EE position/orientation via the correct URDF and tool calibration.
2. Filter outliers, resample timestamps, and smooth position and orientation while preserving clearance constraints.
3. Use a bounded speed profile (quintic or trapezoidal) and compute velocity/acceleration continuity metrics.
4. Check sampled path against joint ranges, singularities, tool collision geometry, and fixture clearance in a calibrated model.

## Phase C: DLS-IK tracking

1. Adapt the provided `DLSVelocityCommander` from a static target to a time-parameterized trajectory in simulation/offline testing.
2. Implement a reviewed velocity-command safety gate: joint range/speed/acceleration caps, timeouts, command dimension checks, feedback freshness, controlled stop.
3. Keep the command route configurable and prevent accidental direct publishing on the physical controller.
4. Test zero motion on missing state, malformed commands, stale feedback and disconnects.

## Phase D: Physical validation and evaluation

Only under an approved, supervised robot procedure: verify emergency stop and slow execution, start with an obstacle-free trial, and progress to wire tracing after tool geometry and electrical contact detection are checked.

For each run log start/end time, route and revision, maximum Cartesian error, joint-speed extrema, contact count, errors, stopping reason and operator notes. Evaluate at least three repeated trials.

## Not yet built

The provided archive does not contain an assignment-specific timestamped teaching recorder, a robust wire-contact acquisition node, a validated free-drive integration, or a complete trajectory replay/trial logger. They remain planned project work.
