# Backend A

Backend A is the first application server in the Phase 1 network.

## Port

3001

## Bind Address

0.0.0.0

This allows Mac 2 to reach the backend over the LAN.

## Endpoints

### GET /

Returns:

Hello from Backend A

Response header:

X-Backend: A

### GET /api/status

Returns:

{
  "backend": "A",
  "status": "healthy"
}

## Run

```bash
npm install
npm start