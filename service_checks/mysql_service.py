"""MySQL service wrapper.

Uses the existing script in `services2/needs-love/mysqlCheck.py`.
"""

from __future__ import annotations

from pathlib import Path

from service_checks._legacy_loader import load_legacy_function, run_and_assess

_MYSQL_FUNC = None


def run(target_ip: str, target_name: str) -> bool:
    """Run existing MySQL check and return boolean status.

    Note: the legacy script may fail depending on dependencies/credentials.
    """
    global _MYSQL_FUNC
    if _MYSQL_FUNC is None:
        try:
            _MYSQL_FUNC = load_legacy_function(
                Path(__file__).resolve().parent.parent / "services2" / "needs-love" / "mysqlCheck.py",
                "mysqlCheck",
            )
        except Exception:
            return False
    return run_and_assess(_MYSQL_FUNC, target_ip)

