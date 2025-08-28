# Demo Script 

1. Setup device with agent installed and UI accessible.
2. Open UI and show initial battery % and top processes.
3. Start demo workload: `sudo bash src/target/run_target.sh` (or simulate heavy app).
4. Show agent applying a profile (e.g., balanced or ultra_save) and point out explanation in audit log.
5. Demonstrate user lock: lock brightness or an app in UI and show agent skipping that action.
6. Show RL CSV being populated (logs/rl_data.csv).
7. Stop workload and show battery runtime estimate improvement.

Narration tips: explain that all decisions are on-device, the agent respects user locks, and logs are auditable.
