"""PING service check."""

from __future__ import annotations

import subprocess


def run(target_ip: str, target_name: str) -> bool:
    """Return True when a single ICMP ping succeeds."""
    cmd = ["ping", "-c", "1", "-W", "2", target_ip]
    try:
        result = subprocess.run(cmd, check=False, capture_output=True, text=True, timeout=5)
        return result.returncode == 0
    except Exception:
        return False

