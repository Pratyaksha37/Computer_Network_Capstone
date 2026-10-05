# Private Network Service Platform

## Computer Networks Course Project — Phase 1

A fully local private network service platform built using four physical macOS laptops connected to the same LAN.

The project demonstrates:

- LAN connectivity
- Private DNS
- HTTP/REST backends
- Reverse proxy
- Round-robin load balancing
- HTTPS/TLS
- HTTP caching
- Packet-level analysis using Wireshark
- Failure diagnosis

---

# Team

| Member | Enrollment Number | Role |
|---|---|---|
| Yogesh Mishra | 2401010518 | Mac 1 — DNS |
| Pratyaksha Shastri | 2401010348 | Mac 2 — Nginx |
| Shiva Sharma | 2401010441 | Mac 3 — Backend A |
| Shagun Singh | 2401010434 | Mac 4 — Backend B |

---

# Infrastructure

**Type 1 — 4 physical macOS laptops on the same LAN**

No cloud infrastructure is required.

---

# Architecture

| Machine | Role | Service | Port |
|---|---|---|---|
| Mac 1 | Private DNS + Client | dnsmasq | 53 |
| Mac 2 | Edge / Reverse Proxy / Load Balancer | nginx | 8080 / 8443 |
| Mac 3 | Backend A | Node.js / Express | 3001 |
| Mac 4 | Backend B + Client | Node.js / Express | 3002 |

---

# Request Flow

```text
Client
   |
   | DNS Query
   v
Mac 1 — dnsmasq
   |
   | app.teamX.test → Mac 2
   v
Mac 2 — nginx
   |
   | HTTPS / TLS
   |
   +----------+----------+
   |                     |
   v                     v
Mac 3                  Mac 4
Backend A              Backend B
:3001                  :3002
