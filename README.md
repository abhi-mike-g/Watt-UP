# Samsung EnnovateX 2025 AI Challenge Submission

**Problem Statement:** On-device Agentic System for Intelligent Battery Optimization

**Team Name:** Watt-UP

**Team Members:**
- Abhidutta Mukund Giri
- Prathamesh Aggarwal
- Varanasi Naga Akhil
- Prakhar Agrawal

## Project Description
An agentic system that intelligently optimizes battery usage for a target application, operating fully on-device, with no reliance on cloud computation. Adaptive, modular, and context-aware, ensuring the target application continues to function effectively while maximizing battery life.

## Project Artefacts (Included)
- `docs/` - Technical documentation in markdown (architecture, implementation, evaluation, security, android integration, demo script)
- `src/` - Source code (agent, ui, scripts, android_sdk)
- `models/` - Placeholder for trained models (instructions to generate/upload)
- `datasets/` - Placeholder for generated RL dataset and instructions
- `installer/` - Installer script to install to `/opt/ondevice-agent/src/` and systemd unit
- `systemd/` - systemd unit file
- `README.md` - Quickstart

## Models Used
- None external. The MVP uses a tabular Q-learning model saved as `models/q_table.pkl` after training.

## Models Published
- (If you want us to publish the trained Q-table to Hugging Face, say so and provide account details or we will provide upload instructions.)

## Datasets Used
- No external datasets used. The agent generates `logs/rl_data.csv` during runtime which can be published.

## Attribution
Third-party libraries used: Flask, psutil, PyYAML, numpy, pandas. See `ATTRIBUTION.md` for details.
