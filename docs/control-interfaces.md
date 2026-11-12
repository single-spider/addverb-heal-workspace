# HEAL control and data interfaces

These are source-observed interfaces that must be checked against the actual running ROS graph. Some are optional or provided by separate lab packages.

| Interface | Direction | Usage and caveat |
| --- | --- | --- |
| `/joint_states` | Robot -> observer | Joint positions and, if published, velocities; map by joint name, check age and completeness. |
| `/robot_description` | Robot/config -> application | URDF used for kinematic chain and FK; validate deployed robot/tool variant. |
| `/velocity_controller/commands` | Application -> controller | Six-joint velocity command topic; **direct publication can bypass the optional safety relay**. |
| `/heal_teleop/raw_commands` | Application -> optional relay | Separate route used by some newer lab experiments; verify relay activation and wiring first. |
| End-effector pose publisher | FK -> observer | Computes end-effector pose from joint states plus URDF, may be a custom topic. |
| `/recorder_controller/record_mode` | Service | Vendor recorder mode switching; sampling timestamps need review. |
| `/recorder_controller/replay_mode` | Action | Vendor trajectory playback, which may not satisfy project-required DLS-IK replay. |
| Gripper control service | Application -> gripper | Custom lab/backend service, actual gripper type and force units must be verified. |

## Imported HEAL starter files

- `Dual_Arm/homing_codes/heal_going_home.py`: example joint-space homing, derived velocity commands.
- `Dual_Arm/sample_ik/heal_dls_ik.py`: example single-arm DLS command-node entry point.
- `utils/dls_velocity_commander.py`: Jacobian-based Cartesian velocity control and target handling.
- `utils/quintic_planner.py`: quintic interpolation utilities.
- `heal_end_effector_pub_node.py`: FK/end-effector pose calculations.
- `utils/gripper_commands/heal_dynamixel_gripper.py`: command interface to the gripper.

The files are maintained unchanged under `starter/heal/` to keep provenance intact. Some examples rely on imports or paths that need adaptation and have not been tested with live hardware.
