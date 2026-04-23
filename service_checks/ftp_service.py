"""FTP service wrapper."""

from __future__ import annotations

from pathlib import Path

from service_checks._legacy_loader import load_legacy_function, run_and_assess

_FTP_FUNC = None


def run(target_ip: str, target_name: str) -> bool:
    """Run existing FTP check and return boolean for reporting."""
    global _FTP_FUNC
    if _FTP_FUNC is None:
        try:
            _FTP_FUNC = load_legacy_function(
                Path(__file__).resolve().parent.parent / "services2" / "FTPCheck.py",
                "FTPCheck",
            )
        except Exception:
            return False
    return run_and_assess(_FTP_FUNC, target_ip)

