# network-recon-tool

A Python network reconnaissance tool that checks service availability per host
and reports:

- Per-check status (`OK` / `FAILED`)
- Per-host success percentage
- Per-service uptime percentage
- Overall success percentage and status color

## How It Works

`main.py` is the orchestrator.

1. `TARGETS` defines which services should exist on each host IP.
2. `SERVICE_RUNNERS` maps service names (for example `SSH`, `MYSQL`) to check
   functions in `service_checks/`.
3. For each host, the tool runs only the services listed for that host.
4. It prints host-level results and computes:
   - Host success %
   - Service uptime %
   - Overall success %

## Project Structure

- `main.py` - orchestration, host-to-service mapping, reporting
- `service_checks/` - one file per service check implementation:
  - `dns_service.py`
  - `ftp_service.py`
  - `imap_service.py`
  - `mysql_service.py`
  - `pop3_service.py`
  - `smtp_service.py`
  - `ssh_service.py`
  - `telnet_service.py`
  - `web_service.py`
  - `ping_service.py` (optional; include in mapping if needed)

## Requirements

- Python 3
- Python packages:
  - `paramiko` (SSH checks)
  - `pymysql` (MySQL checks)

Install dependencies:

```bash
pip install paramiko pymysql
```

## Configure Host-to-Service Mapping

Edit `TARGETS` in `main.py`:

```python
TARGETS = [
    {"ip": "192.168.1.10", "name": "ns.mininet.net", "services": ["SSH", "DNS"]},
    {"ip": "192.168.1.11", "name": "mail.mininet.net", "services": ["SSH", "SMTP", "POP3", "IMAP"]},
    {"ip": "192.168.1.12", "name": "www.mininet.net", "services": ["SSH", "WEB"]},
    {"ip": "192.168.1.13", "name": "db.mininet.net", "services": ["FTP", "SSH", "TELNET", "MYSQL"]},
    {"ip": "192.168.1.14", "name": "store.mininet.net", "services": ["SSH", "WEB"]},
]
```

Only services listed for a host are checked.

## Run

```bash
python main.py
```

## Output

For each host, the program prints lines like:

- `SSH Check OK for: ns.mininet.net`
- `DNS Check FAILED for: ns.mininet.net`
- `Success: 50%`

After all hosts, the program prints:

- `Service Uptime` section (for example `SSH Uptime: 80% (4/5)`)
- `Overall Success: <percent>%`
- `Status: GREEN | YELLOW | RED`

## Notes

- SSH check uses socket connectivity plus Paramiko authentication.
- MySQL check uses PyMySQL login and query execution.
- A service marked `FAILED` means connect/auth/query did not complete
  successfully during that run.
