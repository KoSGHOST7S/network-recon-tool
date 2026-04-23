"""DNS service wrapper.

This file calls your existing `services2/dnsCheck.py` function as-is.
"""

from __future__ import annotations

from pathlib import Path

from service_checks._legacy_loader import load_legacy_function, run_and_assess

_DNS_FUNC = None


def run(target_ip: str, target_name: str, dns_server_ip: str) -> bool:
    """Run legacy DNS check using configured DNS server and host details."""
    global _DNS_FUNC
    if _DNS_FUNC is None:
        try:
            _DNS_FUNC = load_legacy_function(
                Path(__file__).resolve().parent.parent / "services2" / "dnsCheck.py",
                "dnsCheck",
            )
        except Exception:
            return False

    return run_and_assess(_DNS_FUNC, dns_server_ip, target_name, target_ip)

