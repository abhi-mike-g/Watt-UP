import numpy as np, pickle, pathlib, random
MODEL_PATH = pathlib.Path("models/q_table.pkl")

def discretize_state(bat_pct, cpu_pct, pred_tte_min):
    b = min(10, int(bat_pct/10)) if bat_pct>=0 else 10
    c = min(10, int(cpu_pct/10))
    t = min(12, int(pred_tte_min/10)) if pred_tte_min>0 else 12
    return (b,c,t)

ACTIONS = ["ultra_save","balanced","noop"]

class QAgent:
    def __init__(self, alpha=0.1, gamma=0.9, eps=0.1):
        self.alpha = alpha; self.gamma = gamma; self.eps = eps
        self.q = {}
        self.load()

    def load(self):
        if MODEL_PATH.exists():
            with MODEL_PATH.open("rb") as f:
                self.q = pickle.load(f)

    def save(self):
        MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
        with MODEL_PATH.open("wb") as f:
            pickle.dump(self.q, f)

    def get_q(self, s):
        if s not in self.q:
            self.q[s] = np.zeros(len(ACTIONS))
        return self.q[s]

    def choose(self, s):
        if random.random() < self.eps:
            return random.randrange(len(ACTIONS))
        q = self.get_q(s)
        return int(np.argmax(q))

    def update(self, s, a, r, s2):
        q = self.get_q(s)
        q2 = self.get_q(s2)
        q[a] = q[a] + self.alpha * (r + self.gamma * np.max(q2) - q[a])
        self.q[s] = q
