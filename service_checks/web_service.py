"""Web (HTTP) service check."""

from __future__ import annotations

import http.client


def run(target_ip: str, target_name: str) -> bool:
    """Return True when HTTP service responds on port 80."""
    try:
        conn = http.client.HTTPConnection(target_ip, 80, timeout=5)
        conn.request("GET", "/")
        response = conn.getresponse()
        conn.close()
        return 100 <= response.status < 600
    except Exception:
        return False

