#!/usr/bin/env bash
sudo systemd-run --unit=demo.target --scope --property=CPUQuota=80% /usr/bin/python3 -c 'import time
while True:
    [x*x for x in range(1000000)]
    time.sleep(0.5)'
