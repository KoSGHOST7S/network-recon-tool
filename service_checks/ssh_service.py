"""SSH service check using command-line fingerprint trust workflow.

Flow:
1) Run an SSH command as admin with host-key auto-accept enabled.
2) Confirm the host key is present in known_hosts.
3) Report SSH as successful only when fingerprint trust is established.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

SSH_USER = "admin"
KNOWN_HOSTS_FILE = Path.home() / ".ssh" / "known_hosts"

def run(target_ip: str, target_name: str) -> bool:
    """Trust and verify SSH host fingerprint using local ssh/ssh-keygen tools."""
    # Ensure ~/.ssh exists so known_hosts can be written.
    KNOWN_HOSTS_FILE.parent.mkdir(parents=True, exist_ok=True)

    # This command performs first-contact trust (accept-new) and exits.
    # NumberOfPasswordPrompts=0 avoids hanging in non-interactive runs.
    ssh_cmd = [
        "ssh",
        "-o",
        "StrictHostKeyChecking=accept-new",
        "-o",
        f"UserKnownHostsFile={KNOWN_HOSTS_FILE}",
        "-o",
        "ConnectTimeout=5",
        "-o",
        "NumberOfPasswordPrompts=0",
        f"{SSH_USER}@{target_ip}",
        "exit",
    ]

    try:
        subprocess.run(ssh_cmd, check=False, capture_output=True, text=True, timeout=10)
    except Exception:
        return False

    # Confirm the host key now exists in known_hosts.
    verify_cmd = ["ssh-keygen", "-F", target_ip, "-f", str(KNOWN_HOSTS_FILE)]
    try:
        verify = subprocess.run(
            verify_cmd,
            check=False,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except Exception:
        return False

    return verify.returncode == 0 and bool(verify.stdout.strip())

