import json, hmac, hashlib, pathlib, time, csv
LOG_FILE = pathlib.Path("logs/audit.log")
RL_CSV = pathlib.Path("logs/rl_data.csv")
KEY = b"ondevice-secret-key"  # replace with secure store in production

def _sign(prev_sig, payload):
    msg = (prev_sig or "").encode() + json.dumps(payload, sort_keys=True).encode()
    return hmac.new(KEY, msg, hashlib.sha256).hexdigest()

def append(entry:dict):
    LOG_FILE.parent.mkdir(exist_ok=True)
    prev = None
    if LOG_FILE.exists():
        try:
            with LOG_FILE.open("rb") as f:
                last = f.read().splitlines()[-1]
                prev = json.loads(last.decode())["sig"]
        except Exception:
            prev = None
    entry["ts"] = time.time()
    sig = _sign(prev, entry)
    entry["sig"] = sig
    with LOG_FILE.open("ab") as f:
        f.write((json.dumps(entry)+"\n").encode())
    if "rl" in entry:
        RL_CSV.parent.mkdir(exist_ok=True)
        hdr = ["ts","bat_pct","pred_tte_min","cpu_pct","top1_cpu","action","reward"] 
        exists = RL_CSV.exists()
        with RL_CSV.open("a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not exists:
                writer.writerow(hdr)
            r = entry["rl"]
            row = [entry["ts"], r.get("bat_pct"), r.get("pred_tte_min"), r.get("cpu_pct"), r.get("top1_cpu"), r.get("action"), r.get("reward")]
            writer.writerow(row)
