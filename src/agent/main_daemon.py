import time, pathlib, os, sys
# path to be adjusted so imports work when installed to /opt/ondevice-agent/src/
sys.path.append(os.path.dirname(__file__)+"/../")
from src.agent.telemetry import system_snapshot
from src.agent.policy import PolicyEngine
from src.agent.actions import set_brightness_pct, wifi_power_save, set_cgroup_cpu_quota, set_cpu_max_khz
from src.agent.audit import append
from src.agent.policy_rl import QAgent

engine = PolicyEngine()
rl_agent = QAgent()
STATE = {'last_snapshot': None, 'last_actions': []}

def compute_reward(prev_snap, cur_snap, action_name):
    prev_tte = prev_snap.get('pred_tte_min', -1) if prev_snap else -1
    cur_tte = cur_snap.get('pred_tte_min', -1)
    bat_diff = cur_snap['battery'].get('percent', -1) - (prev_snap['battery'].get('percent', -1) if prev_snap else -1)
    cpu_pen = cur_snap['cpu']['cpu_percent']/100.0
    if prev_tte>0 and cur_tte>0:
        r = (cur_tte - prev_tte) - cpu_pen
    else:
        r = -cpu_pen * 0.1 + (bat_diff * 0.01)
    return r

def apply_profile(profile):
    set_brightness_pct(profile.get('brightness_pct',50))
    wifi_power_save(profile.get('wifi_powersave', True))
    set_cpu_max_khz(profile.get('cpu_max_khz', 1400000))

def agent_loop():
    prev = None
    while True:
        snap = system_snapshot()
        STATE['last_snapshot'] = snap
        proposals = engine.propose(snap)
        applied = []
        for a in proposals:
            ok, reason = engine.rule_shield_allows(a)
            if not ok:
                append({'event':'skip_action','action':a,'reason':reason})
                continue
            if a['type']=='apply_profile':
                prof = engine.policy['system_profiles'].get(a['profile'])
                if prof:
                    apply_profile(prof)
                    applied.append(a)
            elif a['type']=='set_quota':
                set_cgroup_cpu_quota(a['unit'], a['quota_pct'])
                applied.append(a)
            append({'event':'apply_action','action':a,'snapshot':snap, 'rl': {'bat_pct': snap['battery'].get('percent'), 'pred_tte_min': snap.get('pred_tte_min'), 'cpu_pct': snap['cpu'].get('cpu_percent'), 'top1_cpu': snap['top_procs'][0]['cpu'] if snap['top_procs'] else 0, 'action': a.get('profile') if a.get('type')=='apply_profile' else 'set_quota', 'reward': 0.0}})
        time.sleep(3)
        new_snap = system_snapshot()
        if applied:
            r = compute_reward(snap, new_snap, applied[-1])
            append({'event':'reward_record','action':applied[-1],'reward': r, 'rl': {'bat_pct': snap['battery'].get('percent'), 'pred_tte_min': snap.get('pred_tte_min'), 'cpu_pct': snap['cpu'].get('cpu_percent'), 'top1_cpu': snap['top_procs'][0]['cpu'] if snap['top_procs'] else 0, 'action': applied[-1].get('profile') if applied[-1].get('type')=='apply_profile' else 'set_quota', 'reward': r}})
        STATE['last_actions'] = applied
        prev = snap

if __name__=='__main__':
    agent_loop()
