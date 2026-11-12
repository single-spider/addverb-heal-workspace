# Project 3: Wire-Trace Trial

Source: the project brief supplied as a Notion export in November 2026. This is a concise, independently written summary rather than a redistribution of the original Notion page.

## Required Stage 1

1. Manually guide the Addverb HEAL end effector (or a calibrated attached probe) along a vertical three-dimensional wire course under an approved free-drive/gravity-compensation procedure.
2. Record the demonstration, including timestamped joint states and ideally tool position/orientation.
3. Filter and interpolate the demonstration into a smooth, feasible trajectory.
4. Replay with damped-least-squares inverse kinematics and ROS 2 joint velocity control.
5. Demonstrate low-contact or contact-free performance, timing, and consistent replay over repeated trials.

## Optional Stage 2

Implement learning/adaptation or an alternative non-hardcoded trajectory approach that can improve after trials or handle variation in the wire geometry. The brief has an inconsistency between its description of the bonus and its marking table; clarify the applicable scoring with the instructor.

## Evidence / deliverables

- Reproducible GitHub repository with setup, teaching, processing, replay, safety and evaluation procedures.
- Public demonstration of Stage 1; Stage 2 if completed.
- Video submission of at most three minutes showing teaching, autonomous replay, and timing.
- Logs for at least three trials: total time, contact indication, completion, trajectory error, and any safety intervention.

## Critical experiment design question

A tool encircling a wire requires a different collision-free reference trajectory than a probe traveling beside the wire. Define the tool's actual shape and the intended clearance geometry before applying radial offsets or spline smoothing. The task brief's 2–5 mm figure is a target requiring physical measurement and calibration, not an established safe clearance.
