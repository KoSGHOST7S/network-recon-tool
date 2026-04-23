"""DNS service check.

Direct check implementation: test whether TCP 53 is reachable on the host.
"""

from __future__ import annotations

import socket


def run(target_ip: str, target_name: str) -> bool:
    """Return True when DNS service port is reachable."""
    try:
        with socket.create_connection((target_ip, 53), timeout=5):
            return True
    except OSError:
        return False

