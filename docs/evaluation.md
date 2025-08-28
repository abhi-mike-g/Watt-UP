# Evaluation Plan

Baselines:
- No-agent (default OS behavior)
- Aggressive power saver (OS-level)

Metrics:
- Battery runtime extension (%) under synthetic workloads
- Application performance retention (% vs baseline)
- Thermal profile (max CPU temp)
- Decision latency and number of user reverts

Test scenarios:
- Continuous CPU-bound workload
- Mixed workload (periodic bursts)
- Idle with background sync apps

Reproducibility:
- Use [target/run_target.sh](https://github.com/abhi-mike-g/Watt-UP/blob/main/src/target/run_target.sh) to generate load and follow [docs/demo_script.md](https://github.com/abhi-mike-g/Watt-UP/blob/main/docs/demo_script.md) to collect logs.
