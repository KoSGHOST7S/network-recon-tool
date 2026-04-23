"""FTP service check."""

from __future__ import annotations

import socket


def run(target_ip: str, target_name: str) -> bool:
    """Return True when FTP service port is reachable."""
    try:
        with socket.create_connection((target_ip, 21), timeout=5):
            return True
    except OSError:
        return False

