# TLS Setup

Mac 2 terminates HTTPS using nginx.

## Certificate

A self-signed certificate is generated using OpenSSL.

Example:

```bash
mkdir -p ~/nginx-certs

openssl req -x509 -nodes -days 365 \
-newkey rsa:2048 \
-keyout ~/nginx-certs/teamX.key \
-out ~/nginx-certs/teamX.crt \
-subj "/CN=app.teamX.test"