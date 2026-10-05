# Network Inventory

| Machine | Role | IP Address | Service | Port |
|---|---|---|---|---|
| Mac 1 | DNS + Client | 10.7.11.107 | dnsmasq | 53 |
| Mac 2 | Edge / Load Balancer | 10.7.11.110 | nginx | 8080 / 8443 |
| Mac 3 | Backend A | 10.7.11.108 | Node.js | 3001 |
| Mac 4 | Backend B | 10.7.11.109 | Node.js | 3002 |

                    Private LAN / Wi-Fi
                           |
        +------------------+------------------+
        |                  |                  |
      Mac 1              Mac 2              Mac 3
   Private DNS         nginx Edge         Backend A
    + Client         HTTPS / LB            :3001
        |              :8443
        |                 |
        |          +------+------+
        |          |             |
        |       Backend A     Backend B
        |        Mac 3         Mac 4
        |        :3001         :3002
        |          |             |
        +----------+-------------+
                   |
                 Client