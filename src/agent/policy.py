import yaml, pathlib, time
POL = pathlib.Path("src/configs/policy.yaml")  # note: when running from repo root, this path resolves to src/configs

def load_policy():
    return yaml.safe_load(POL.read_text())

class PolicyEngine:
    def __init__(self):
        self.reload()

    def reload(self):
        self.policy = load_policy()

    def is_user_locked(self, key):
        ap = self.policy.get("app_policies", {})
        if key in ap:
            return ap[key].get("user_locked", False)
        return False

    def rule_shield_allows(self, action):
        if action.get("target") and self.is_user_locked(action["target"]):
            return False, "user_locked"
        return True, "ok"

    def propose(self, snapshot):
        p = self.policy
        bat = snapshot["battery"].get("percent", -1)
        cpu = snapshot["cpu"]["cpu_percent"]
        actions = []
        if bat >=0 and bat <= p["global"]["critical_battery_pct"]:
            actions.append({"type":"apply_profile","profile":"ultra_save","target":"system_profile"})
            return actions
        if bat <= p["global"]["low_battery_pct"] or cpu>70:
            actions.append({"type":"apply_profile","profile":"balanced","target":"system_profile"})
            for proc in snapshot["top_procs"][2:6]:
                actions.append({"type":"set_quota","unit":f"app-{proc['pid']}.slice","quota_pct":40,"target":proc["name"]})
        return actions
