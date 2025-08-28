### **Important Instructions**:  
- Click on *"Use this template"* button and *"Create a new repository"* in your github account for submission.
<img width="1262" height="93" alt="Screenshot 2025-08-15 at 5 59 49 AM" src="https://github.com/user-attachments/assets/b72d5afd-ba07-4da1-ac05-a373b3168b6a" />

- Add one of the following open source licenses - [MIT](https://opensource.org/licenses/MIT), [Apache 2.0](https://opensource.org/licenses/Apache-2.0) or [BSD 3-Clause](https://opensource.org/licenses/BSD-3-Clause) to your submission repository. 
- Once your repository is ready for **evaluation** send an email to ennovatex.io@samsung.com with the subject - "AI Challenge Submission - Team name" and the body of the email must contain only the Team Name, Team Leader Name & your GitHub project repository link.
- All submission project materials outlined below must be added to the github repository and nothing should be attached in the submission email.
- In case of any query, please feel free to reach out to us at ennovatex.io@samsung.com

#### Evaluation Criteria

| Project Aspect | % |
| --- | --- |
| Novelty of Approach | 25% |
| Technical implementation & Documentation | 25% |
| UI/UX Design or User Interaction Design | 15% |
| Ethical Considerations & Scalability | 10% |
| Demo Video (10 mins max) | 25% |

**-------------------------- Your Project README.md should start from here -----------------------------**

# Samsung EnnovateX 2025 AI Challenge Submission

**Problem Statement:** On-device Agentic System for Intelligent Battery Optimization

**Team Name:** Watt-UP

**Team Members:**
- Abhidutta Mukund Giri
- Prathamesh Aggarwal
- Varanasi Naga Akhil
- Prakhar Agrawal

**Demo Video Link:** (PLACEHOLDER — upload to YouTube and paste link here)

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

## Datasets Published
- (Placeholder) You may publish `logs/rl_data.csv` to Hugging Face datasets following `datasets/README.md` instructions.

## Attribution
Third-party libraries used: Flask, psutil, PyYAML, numpy, pandas. See `ATTRIBUTION.md` for details.
