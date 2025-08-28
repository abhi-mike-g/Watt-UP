# Implementation Details

Source layout (src/):
- src/agent/telemetry.py
- src/agent/actions.py
- src/agent/policy.py
- src/agent/policy_rl.py
- src/agent/audit.py
- src/agent/main_daemon.py
- src/ui/flask_ui.py
- src/scripts/train_q.py
- src/installer/install.sh
- src/systemd/ondevice-agent.service
- src/android_sdk/*

Notes:
- The system is designed for Linux SBCs; sysfs paths and commands may vary. Adjust `/sys/devices/system/cpu` or backlight paths as needed.
- The installer copies files to `/opt/ondevice-agent/src/` and registers systemd unit.

Runtime behavior:
- The daemon polls telemetry, proposes actions, checks rule shield, applies permitted actions, and logs audits and RL rows.
