import contextlib
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from time import sleep

HOST = "0.0.0.0"
PORT = 8080
MESSAGE_API = os.getenv('MESSAGE')


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        message = "Hello World!"

        self.wfile.write(bytes(message, "utf-8"))


def run(host, port, server_class=HTTPServer, handler_class=Handler):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)

    with contextlib.suppress(KeyboardInterrupt):
        httpd.serve_forever()

    httpd.server_close()


if __name__ == "__main__":
    sleep(10)
    print("Starting server...")
    run(HOST, PORT)
