# HEAL-only sample code from the Project 3 starter archive

These seven Python files are copied from the user-provided **MIT-licensed** RC-DS starter package and retain their original layout beneath `starter/heal`. See the repository root `LICENSE` for attribution.

**They preserve the supplied logic, with one machine-specific path redacted, not validated hardware operating instructions.** `heal_going_home.py` and `heal_dls_ik.py` can publish directly to a live robot velocity controller. The sample IK file may need its relative Python import-root calculation corrected when used in this new layout. Gripper example invocation may issue a physical action. Do not execute any of these on HEAL without an approved operator procedure.

The original starter README was intentionally omitted because it contained a plaintext machine password and specific internal deployment commands. Obtain current credentials and operating instructions from the lab administrator.

Imported paths:

```text
starter/heal/
  Dual_Arm/homing_codes/heal_going_home.py
  Dual_Arm/sample_ik/heal_dls_ik.py
  heal_end_effector_pub_node.py
  utils/__init__.py
  utils/dls_velocity_commander.py
  utils/quintic_planner.py
  utils/gripper_commands/heal_dynamixel_gripper.py
```
