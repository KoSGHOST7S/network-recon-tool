"""SSH service wrapper."""

from __future__ import annotations

from pathlib import Path

from service_checks._legacy_loader import load_legacy_function, run_and_assess

_SSH_FUNC = None


def run(target_ip: str, target_name: str) -> bool:
    """Run existing SSH check and return True/False to main."""
    global _SSH_FUNC
    if _SSH_FUNC is None:
        try:
            _SSH_FUNC = load_legacy_function(
                Path(__file__).resolve().parent.parent / "services2" / "SSHCheck.py",
                "SSHCheck",
            )
        except Exception:
            return False
    return run_and_assess(_SSH_FUNC, target_ip)

