#!/usr/bin/env python3
"""Network recon orchestrator.

This script runs service checks per host using a mapping you can edit.
Each service check lives in its own file under `service_checks/` so you can
learn how each one works independently.
"""

from __future__ import annotations

from typing import Callable

from service_checks import (
    dns_service,
    mysql_service,
    ssh_service,
    telnet_service,
    web_service,
)

# ---------------------------------------------------------------------------
# Configuration you can edit
# ---------------------------------------------------------------------------
# DNS server used by the legacy dnsCheck function.
DNS_SERVER_IP = "192.168.1.10"

# Each host has an IP, display name, and list of checks to run.
# Rule: only include checks for services that host actually exposes.
# Example: 192.168.1.10 has only SSH (22) and DNS (53).
TARGETS = [
    {"ip": "192.168.1.10", "name": "ns.mininet.net", "services": ["SSH", "DNS"]},
    {"ip": "192.168.1.11", "name": "mail.mininet.net", "services": ["SSH"]},
    {"ip": "192.168.1.12", "name": "www.mininet.net", "services": ["SSH", "WEB"]},
    {"ip": "192.168.1.13", "name": "db.mininet.net", "services": ["SSH", "TELNET", "MYSQL"]},
    {"ip": "192.168.1.14", "name": "store.mininet.net", "services": ["SSH", "WEB"]},
]


def run_dns(ip: str, name: str) -> bool:
    """Adapter for DNS check because legacy function needs 3 arguments."""
    return dns_service.run(ip, name, DNS_SERVER_IP)


SERVICE_RUNNERS: dict[str, Callable[[str, str], bool]] = {
    "DNS": run_dns,
    "MYSQL": mysql_service.run,
    "WEB": web_service.run,
    "SSH": ssh_service.run,
    "TELNET": telnet_service.run,
}


def score_to_status(score: float) -> str:
    """Translate numeric percentage to color-like status label."""
    if score >= 95:
        return "GREEN"
    if score >= 75:
        return "YELLOW"
    return "RED"


def run_target(ip: str, name: str, services: list[str]) -> float:
    """Run all configured services for one host and print host summary."""
    passed = 0

    for service in services:
        runner = SERVICE_RUNNERS.get(service)
        if runner is None:
            print(f"{service} Check FAILED for: {name}")
            continue

        ok = runner(ip, name)
        status = "OK" if ok else "FAILED"
        print(f"{service} Check {status} for: {name}")
        if ok:
            passed += 1

    success = (passed / len(services)) * 100 if services else 0
    print(f"Success: {success:.0f}%\n")
    return success


def main() -> None:
    """Program entrypoint."""
    host_scores = []

    for target in TARGETS:
        host_scores.append(run_target(target["ip"], target["name"], target["services"]))

    overall = sum(host_scores) / len(host_scores) if host_scores else 0
    print(f"Overall Success: {overall:.0f}%")
    print(f"Status: {score_to_status(overall)}")


if __name__ == "__main__":
    main()

