#!/usr/bin/env python3
"""Reference reconstruction of Backend A; not an export of deployed source."""

import hashlib
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = "0.0.0.0"
PORT = 3001
BACKEND = "A"


class Handler(BaseHTTPRequestHandler):
    def send_body(self, status, body, content_type, cache_control, etag=None):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Backend", BACKEND)
        self.send_header("Cache-Control", cache_control)
        if etag:
            self.send_header("ETag", etag)
        self.end_headers()
        if self.command != "HEAD" and status != 304:
            self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/status":
            body = json.dumps(
                {"backend": BACKEND, "status": "ok", "port": PORT},
                separators=(",", ":"),
            ).encode()
            self.send_body(200, body, "application/json", "no-store")
            return

        if self.path == "/":
            body = b"Hello from Backend A\n"
            etag = '"' + hashlib.sha256(body).hexdigest()[:16] + '"'
            if self.headers.get("If-None-Match") == etag:
                self.send_body(304, b"", "text/plain", "public, max-age=30", etag)
                return
            self.send_body(200, body, "text/plain", "public, max-age=30", etag)
            return

        self.send_body(404, b"Not Found\n", "text/plain", "no-store")

    do_HEAD = do_GET


if __name__ == "__main__":
    print(f"Backend {BACKEND} listening on {HOST}:{PORT}")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
