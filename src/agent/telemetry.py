import psutil, pathlib, time
def read_file(path):
    try:
        return pathlib.Path(path).read_text().strip()
    except Exception:
        return None

def battery_info():
    base = "/sys/class/power_supply/BAT0"
    if pathlib.Path(base).exists():
        cap = read_file(f"{base}/capacity")
        status = read_file(f"{base}/status")
        volt = read_file(f"{base}/voltage_now")
        temp = read_file(f"{base}/temp")
        return {
            "percent": int(cap) if cap else -1,
            "status": status,
            "voltage_v": int(volt)/1e6 if volt else None,
            "temp_c": (int(temp)/10) if temp else None
        }
    else:
        b = psutil.sensors_battery()
        return {"percent": int(b.percent) if b else -1, "status": getattr(b, 'power_plugged', None)}

def cpu_gpu_info():
    cpu_perc = psutil.cpu_percent(interval=None)
    cpu_count = psutil.cpu_count()
    freqs = []
    for i in range(cpu_count):
        f = read_file(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_cur_freq")
        freqs.append(int(f)/1000 if f else None)
    temps = psutil.sensors_temperatures()
    return {"cpu_percent": cpu_perc, "cpu_freqs_mhz": freqs, "temps": temps}

def top_processes(n=8):
    procs = []
    for p in psutil.process_iter(["pid","name","username","cpu_percent","memory_info","io_counters"]):
        try:
            info = p.info
            procs.append({
                "pid": info["pid"], "name": info["name"], "cpu": info["cpu_percent"],
                "mem_mb": info["memory_info"].rss/1024/1024 if info["memory_info"] else None
            })
        except Exception:
            pass
    procs.sort(key=lambda x: x["cpu"], reverse=True)
    return procs[:n]

def estimate_runtime_minutes(snapshot):
    bat = snapshot.get("battery_history", [])
    if len(bat) < 2:
        return None
    (t0, p0), (t1, p1) = bat[-2], bat[-1]
    if p0 <= p1:
        return None
    rate_per_sec = (p0 - p1) / (t1 - t0)
    if rate_per_sec <= 0:
        return None
    minutes_left = (p1) / (rate_per_sec) / 60.0
    return max(0, minutes_left)

def system_snapshot(stateful=None):
    if stateful is None:
        stateful = {"battery_history": []}
    snap = {
        "ts": time.time(),
        "battery": battery_info(),
        "cpu": cpu_gpu_info(),
        "top_procs": top_processes()
    }
    bh = stateful.setdefault("battery_history", [])
    bh.append((snap["ts"], snap["battery"].get("percent", -1)))
    while len(bh) > 6:
        bh.pop(0)
    snap["battery_history"] = list(bh)
    snap["pred_tte_min"] = estimate_runtime_minutes(snap) or -1
    return snap
