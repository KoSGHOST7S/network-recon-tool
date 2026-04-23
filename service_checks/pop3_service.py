"""POP3 service check."""

from __future__ import annotations

import socket


def run(target_ip: str, target_name: str) -> bool:
    """Return True when POP3 service port is reachable."""
    try:
        with socket.create_connection((target_ip, 110), timeout=5):
            return True
    except OSError:
        return False

