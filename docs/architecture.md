# Architecture

The system follows a modular architecture:

```
[Telemetry Sources] -> [State Preprocessor] -> [Policy Engine (Rule Shield + RL)] -> [Action Executor]
                                    |-> [Audit & Explainability DB]
                                    |-> [User Control UI / API]
```

Components:
- Telemetry: collects battery, CPU, process stats, sensors.
- Policy Engine: Rule shield that enforces user-locks + adaptive agent (heuristic -> RL).
- Action Executor: writes sysfs, systemd properties, Wi-Fi power-save, and cgroup quotas.
- Audit DB: append-only HMAC-chained logs and RL CSV for training.
- UI: Flask-based local UI for transparency and locking.
