# Security & Privacy

- All processing occurs on-device; logs are stored locally by default.
- Audit logs are signed with an HMAC chain (see [src/agent/audit.py](https://github.com/abhi-mike-g/Watt-UP/blob/main/src/agent/audit.py)) to detect tampering.
- User locks are enforced via policy and require local auth to change (UI/extension).
- Installer runs as root for sysfs access in MVP; recommend creating a limited-privilege helper in production.
