# Addverb HEAL | Wire-Trace Workspace

An evidence-based, **HEAL-focused** workspace for Project 3, the *Wire-Trace Trial*. The aim is to teach a path by manually guiding HEAL, record joint/pose data, process a smooth trajectory, and autonomously replay it with damped-least-squares inverse kinematics (DLS-IK) and ROS 2 velocity control. Repeatability, tool clearance, and safety validation are part of the project.

> **Hardware safety:** All imported motion examples are **reference code, not validated deployment procedures**. Some publish directly to `/velocity_controller/commands`, bypassing an optional safety relay. Do not run them on a connected robot without an approved lab procedure, verified safety systems and joint limits, an appropriate tool model, and a supervised, reduced-speed validation plan. Starting the vendor hardware interface may power on the robot.

## Where to start

| Path | Purpose |
| --- | --- |
| [`docs/project-scope.md`](docs/project-scope.md) | Assignment goals and evaluation criteria |
| [`docs/system-architecture.md`](docs/system-architecture.md) | HEAL ROS 2 control chain and known dependencies |
| [`docs/control-interfaces.md`](docs/control-interfaces.md) | Joint feedback, end-effector FK, velocity commands, gripper, free-drive |
| [`docs/safety-and-open-questions.md`](docs/safety-and-open-questions.md) | Source-identified hazards and information to verify in the lab |
| [`docs/implementation-roadmap.md`](docs/implementation-roadmap.md) | Teaching, processing, DLS tracking, evaluation stages |
| [`starter/heal/`](starter/heal/) | Original HEAL-relevant example Python files (MIT, preserved) |
| [`tools/validate_teach_csv.py`](tools/validate_teach_csv.py) | Offline CSV validator; no robot connection or ROS execution |
| [`data/`](data/) | Data schema and documentation; no real experiments uploaded yet |
| [`docs/provenance.md`](docs/provenance.md) | Source attribution, included/excluded files and publication boundaries |

## Project flow

```text
Approved manual guidance / free drive
    -> read joint-state samples with timestamps
    -> compute/record end-effector poses
    -> filter, resample, interpolate, validate clearances
    -> DLS-IK trajectory tracking in offline/simulation tests
    -> supervised reduced-speed hardware trials
    -> report time, contacts, three-run repeatability
```

The trajectory should use the measured tool geometry and a known coordinate frame. No software-only approximation can establish the real wire clearance without calibration.

## Offline data validation

```bash
python3 tools/validate_teach_csv.py data/path_to_recording.csv
python3 -m unittest discover -s tests -v
```

The validator **reads a local CSV only**. It never opens a ROS topic, connects to the robot or sends any command.

## Status

- Available: supplied HEAL sample code for homing, DLS-IK, FK/pose publishing, quintic trajectory generation, and Dynamixel gripper calls.
- Documented from the local robot-PC archive: HEAL ROS 2 velocity controller, hardware interface, optional velocity safety relay, recorder/free-drive components.
- Not included: proprietary vendor source, compiled backends, machine credentials, raw robot logs, personal home directory snapshots, Franka/bimanual research code, or the unredacted startup instructions.
- Pending: manufacturer safety definitions, last known working deployment, true joint/tool limits, manual-teaching protocol, and safe command routing.

## License and provenance

The provided starter Python code is MIT-licensed, copyright RC-DS (2024). Its MIT license is retained at [`LICENSE`](LICENSE). New documentation and offline tools in this repository are provided under the same MIT terms unless stated otherwise. The Addverb HEAL name is used descriptively; this is not an official manufacturer distribution.
