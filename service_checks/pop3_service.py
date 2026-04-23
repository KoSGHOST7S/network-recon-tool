"""POP3 service wrapper."""

from __future__ import annotations

from pathlib import Path

from service_checks._legacy_loader import load_legacy_function, run_and_assess

_POP_FUNC = None


def run(target_ip: str, target_name: str) -> bool:
    """Run existing POP3 check and return True/False."""
    global _POP_FUNC
    if _POP_FUNC is None:
        try:
            _POP_FUNC = load_legacy_function(
                Path(__file__).resolve().parent.parent / "services2" / "POPCheck.py",
                "POPCheck",
            )
        except Exception:
            return False
    return run_and_assess(_POP_FUNC, target_ip)

