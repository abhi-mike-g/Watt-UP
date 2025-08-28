# Usage

1. Configure policy: edit [src/configs/policy.yaml](https://github.com/abhi-mike-g/Watt-UP/blob/main/src/configs/policy.yaml) to set thresholds and user-locked apps.
2. Install: `sudo bash src/installer/install.sh` (this will place files in `/opt/ondevice-agent/src/`).
3. Start: `sudo systemctl start ondevice-agent`
4. UI: `http://<device-ip>:5000` shows audit log and locks.
5. Generate RL data: run [src/target/run_target.sh](https://github.com/abhi-mike-g/Watt-UP/blob/main/src/target/run_target.sh) to spawn a demo workload.
6. Train Q-table: `python3 src/scripts/train_q.py` (outputs `models/q_table.pkl`).
