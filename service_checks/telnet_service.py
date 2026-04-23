"""Telnet service wrapper."""

from __future__ import annotations

from pathlib import Path

from service_checks._legacy_loader import load_legacy_function, run_and_assess

_TELNET_FUNC = None


def run(target_ip: str, target_name: str) -> bool:
    """Run legacy Telnet check and return True/False for reporting."""
    global _TELNET_FUNC
    if _TELNET_FUNC is None:
        try:
            _TELNET_FUNC = load_legacy_function(
                Path(__file__).resolve().parent.parent
                / "services2"
                / "needs-love"
                / "TelnetCheck.py",
                "connScan",
            )
        except Exception:
            return False

    return run_and_assess(_TELNET_FUNC, target_ip)

