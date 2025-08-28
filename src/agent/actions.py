import pathlib, subprocess, logging, psutil
LOG = logging.getLogger("actions")

def set_cpu_max_khz(khz:int):
    for i in range(0, psutil.cpu_count()):
        p = pathlib.Path(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_max_freq")
        if p.exists():
            try:
                p.write_text(str(khz))
            except Exception as e:
                LOG.warning("CPU freq write failed: %s", e)

def set_brightness_pct(pct:int):
    base = pathlib.Path("/sys/class/backlight")
    if not base.exists(): return False
    for d in base.iterdir():
        maxp = d / "max_brightness"
        curp = d / "brightness"
        try:
            maxv = int(maxp.read_text().strip())
            new = int(max(1, min(maxv, round(maxv * pct / 100.0))))
            curp.write_text(str(new))
        except Exception:
            continue
    return True

def wifi_power_save(enable:bool):
    try:
        subprocess.run(["iw", "dev", "wlan0", "set", "power_save", "on" if enable else "off"],
                       check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False

def set_cgroup_cpu_quota(unit_name:str, quota_pct:int):
    try:
        subprocess.run(["systemctl", "set-property", unit_name, f"CPUQuota={quota_pct}%"], check=False)
        return True
    except Exception:
        return False
