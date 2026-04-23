"""IMAP service wrapper.

This file calls your existing `services2/IMAPCheck.py` function as-is.
"""

from __future__ import annotations

from pathlib import Path

from service_checks._legacy_loader import load_legacy_function, run_and_assess

_IMAP_FUNC = None


def run(target_ip: str, target_name: str) -> bool:
    """Run legacy IMAP check and return boolean result for reporting."""
    global _IMAP_FUNC
    if _IMAP_FUNC is None:
        try:
            _IMAP_FUNC = load_legacy_function(
                Path(__file__).resolve().parent.parent / "services2" / "IMAPCheck.py",
                "IMAPCheck",
            )
        except Exception:
            return False
    return run_and_assess(_IMAP_FUNC, target_ip)

