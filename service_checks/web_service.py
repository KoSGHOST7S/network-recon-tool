"""Web (HTTP) service wrapper."""

from __future__ import annotations

from pathlib import Path

from service_checks._legacy_loader import load_legacy_function, run_and_assess

_WEB_FUNC = None


def run(target_ip: str, target_name: str) -> bool:
    """Run existing web check and return True when call completes."""
    global _WEB_FUNC
    if _WEB_FUNC is None:
        try:
            _WEB_FUNC = load_legacy_function(
                Path(__file__).resolve().parent.parent / "services2" / "WebCheck2.py",
                "WebCheck",
            )
        except Exception:
            return False
    return run_and_assess(_WEB_FUNC, target_ip)

