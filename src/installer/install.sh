#!/usr/bin/env bash
set -e
PKG_DIR="$(dirname "$0")/.."
PKG_DIR="$(realpath "$PKG_DIR")"
echo "Installing On-Device Agent package to /opt/ondevice-agent/src/"
python3 -m pip install --upgrade pip
python3 -m pip install -r "$PKG_DIR/../requirements.txt"
sudo mkdir -p /opt/ondevice-agent
sudo rsync -a "$PKG_DIR/../src/" /opt/ondevice-agent/src/
sudo rsync -a "$PKG_DIR/../systemd/" /opt/ondevice-agent/systemd/
sudo cp "$PKG_DIR/../systemd/ondevice-agent.service" /etc/systemd/system/ondevice-agent.service
sudo systemctl daemon-reload
sudo systemctl enable ondevice-agent.service
echo "Installed. Start the service with: sudo systemctl start ondevice-agent.service"
echo "UI available at http://localhost:5000 (when ui/flask_ui.py is run or as configured)"
