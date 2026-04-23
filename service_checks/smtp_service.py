"""SMTP service wrapper."""

from __future__ import annotations

from pathlib import Path

from service_checks._legacy_loader import load_legacy_function, run_and_assess

_SMTP_FUNC = None


def run(target_ip: str, target_name: str) -> bool:
    """Run existing SMTP check and return boolean status."""
    global _SMTP_FUNC
    if _SMTP_FUNC is None:
        try:
            _SMTP_FUNC = load_legacy_function(
                Path(__file__).resolve().parent.parent / "services2" / "SMTPCheck.py",
                "SMTPCheck",
            )
        except Exception:
            return False
    return run_and_assess(_SMTP_FUNC, target_ip)

