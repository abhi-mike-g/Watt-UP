import pandas as pd, numpy as np, pathlib, pickle
from src.agent.policy_rl import QAgent, discretize_state, ACTIONS

LOG = pathlib.Path('logs/rl_data.csv')
if not LOG.exists():
    print('No RL CSV found at logs/rl_data.csv - run agent to generate data first.')
    raise SystemExit(1)
df = pd.read_csv(LOG)
agent = QAgent(alpha=0.2, gamma=0.95, eps=0.05)
for i in range(len(df)-1):
    r0 = df.iloc[i]; r1 = df.iloc[i+1]
    s = discretize_state(r0['bat_pct'] if not np.isnan(r0['bat_pct']) else -1, r0['cpu_pct'], r0['pred_tte_min'] if not np.isnan(r0['pred_tte_min']) else -1)
    s2 = discretize_state(r1['bat_pct'] if not np.isnan(r1['bat_pct']) else -1, r1['cpu_pct'], r1['pred_tte_min'] if not np.isnan(r1['pred_tte_min']) else -1)
    try:
        a = ACTIONS.index(r0['action']) if r0['action'] in ACTIONS else ACTIONS.index('noop')
    except Exception:
        a = ACTIONS.index('noop')
    r = r0.get('reward', 0.0) if not np.isnan(r0.get('reward', 0.0)) else 0.0
    agent.update(s,a,r,s2)
agent.save()
print('Trained Q-table saved to models/q_table.pkl')
