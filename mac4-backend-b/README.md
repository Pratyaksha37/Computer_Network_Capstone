# Backend B

Backend B is the second application server in the Phase 1 network.

## Port

3002

## Bind Address

0.0.0.0

This allows Mac 2 to reach the backend over the LAN.

## Endpoints

### GET /

Returns:

Hello from Backend B

Response header:

X-Backend: B

### GET /api/status

Returns:

{
  "backend": "B",
  "status": "healthy"
}

## Run

```bash
npm install
npm start