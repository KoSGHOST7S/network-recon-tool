"""PING service wrapper.

This file calls your existing `services2/pingCheck.py` function as-is.
"""

from __future__ import annotations

from pathlib import Path

from service_checks._legacy_loader import load_legacy_function, run_and_assess

_PING_FUNC = None


def run(target_ip: str, target_name: str) -> bool:
    """Run legacy ping check and report success/failure to main."""
    global _PING_FUNC
    if _PING_FUNC is None:
        try:
            _PING_FUNC = load_legacy_function(
                Path(__file__).resolve().parent.parent / "services2" / "pingCheck.py",
                "pingCheck",
            )
        except Exception:
            return False
    return run_and_assess(_PING_FUNC, target_ip)

