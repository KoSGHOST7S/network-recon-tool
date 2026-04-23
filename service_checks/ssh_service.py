"""SSH service check.

Implements the same approach as your provided `SSHCheck.py`:
- Validate TCP connectivity to port 22
- Attempt SSH auth with paramiko using system host keys
"""

from __future__ import annotations

import socket

import paramiko

SSH_USER = "admin"
SSH_PASSWORD = "admin"
SSH_PORT = 22

def run(target_ip: str, target_name: str) -> bool:
    """Return True only when socket and SSH authentication both succeed."""
    conn_socket = None
    ssh_client = None

    try:
        # 1) Low-level TCP connectivity check (matches your script pattern).
        conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_socket.settimeout(5.0)
        conn_socket.connect((target_ip, SSH_PORT))
        conn_socket.close()
        conn_socket = None

        # 2) Paramiko SSH check with system host keys and admin credentials.
        ssh_client = paramiko.SSHClient()
        ssh_client.load_system_host_keys()
        ssh_client.connect(target_ip, SSH_PORT, SSH_USER, SSH_PASSWORD, timeout=5.0)
        return True
    except Exception:
        return False
    finally:
        if ssh_client is not None:
            ssh_client.close()
        if conn_socket is not None:
            conn_socket.close()

