# Phase 1 Test Plan

## 1. LAN Connectivity
- IP addresses of all 4 Macs
- Ping tests
- Expected results

## 2. Private DNS
- dnsmasq configuration
- dig app.teamX.test
- dig api.teamX.test
- Public DNS NXDOMAIN test

## 3. Backend Tests
### Backend A
- GET /
- GET /api/status

### Backend B
- GET /
- GET /api/status

## 4. Nginx Load Balancing
- HTTPS request
- Repeated requests
- X-Backend alternates A/B

## 5. TLS
- Certificate verification
- TLS version
- No curl -k

## 6. HTTP Caching
- Cache-Control
- ETag
- 304 / conditional request evidence if demonstrated

## 7. Failure Scenario
- Option A: Stop Backend A
- Before
- Action
- After
- Restoration