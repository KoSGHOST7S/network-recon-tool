"""MySQL service check.

Direct check implementation: test whether TCP 3306 is reachable.
"""

from __future__ import annotations

import socket


def run(target_ip: str, target_name: str) -> bool:
    """Return True when MySQL service port is reachable."""
    try:
        with socket.create_connection((target_ip, 3306), timeout=5):
            return True
    except OSError:
        return False

