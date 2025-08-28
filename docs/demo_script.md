# Demo Script

1. Setup device with agent installed and UI accessible.
2. Open UI and observe initial battery % and top processes.
3. Start demo workload: `sudo bash src/target/run_target.sh` (or simulate heavy app).
4. Agent applies a profile (e.g., balanced or ultra_save) and points out explanation in audit log.
5. Demonstration of user lock: lock brightness or an app in UI and Agent skips that action.
6. RL CSV is being populated (logs/rl_data.csv).
7. Stop workload and observe battery runtime estimate improvement.

All decisions are on-device, the agent respects user locks, and logs are auditable.
