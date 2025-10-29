#!/usr/bin/env python3
"""
Simple HTTP server for Split Lease static pages
Serves the pages directory on the configured port
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.resolve()
PAGES_DIR = SCRIPT_DIR / "pages"

# Read port from .ports.env if it exists
PORT = 9212  # Default port
ports_env = SCRIPT_DIR.parent.parent / ".ports.env"

if ports_env.exists():
    with open(ports_env) as f:
        for line in f:
            if line.startswith("FRONTEND_PORT="):
                PORT = int(line.split("=")[1].strip())
                break

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PAGES_DIR), **kwargs)

    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    if not PAGES_DIR.exists():
        print(f"Error: Pages directory not found at {PAGES_DIR}")
        sys.exit(1)

    print(f"Starting server on port {PORT}...")
    print(f"Serving files from: {PAGES_DIR}")
    print(f"\nSearch page available at:")
    print(f"  http://localhost:{PORT}/search/")
    print(f"\nPress Ctrl+C to stop the server")

    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nShutting down server...")
            httpd.shutdown()

if __name__ == "__main__":
    main()
