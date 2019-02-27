from http.server import HTTPServer, BaseHTTPRequestHandler
from cowpy import cow
from urllib.parse import urlparse, parse_qs


cheese = cow.Moose()
msg = cheese.milk('My whitty message')


class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == ('/'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f'<!DOCTYPE html><html><head><title>cowsay</title><head><body><header><nav><ul><li><a href="/cow">cowsay</a></li><ul></nav><header><main> project description defining how users can further interact with the application </main></body></html>'.encode())
            return

        elif parsed_path.path == ('/cow'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('hello'.encode())
            return
        elif parsed_path.path == ('/cowxxxxx'):

            self.wfile.write(b'we did the thing with the qs')
            try:

                cat = parsed_qs['category'][0]
                self.wfile.write(b'we did the thing with the qs')
            except KeyError:
                self.send_response_only(400)
                self.end_headers()
                return

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'we did the thing with the qs')
            return
        # elif parsed_path.path == '/cow':
        #     try:
        #         cat = parsed_qs['category'][0]
        #     except KeyError:
        #         self.send_response_only(400)
        #         self.end_headers()
        #         return

            cheese = cow.Moose()
            msg = cheese.milk('{parsed_qs.text[0]}')

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f'<!DOCTYPE html><html><head><title>cowsay</title><head><body><header><nav><ul><li><a href=“/cow”>cowsay</a></li><ul></nav><header><main> <pre>{msg}</pre> project description defining how users can further interact with the application </main></body></html>'.encode())
            return

def run_forever():
    port = 5000
    server_address = ('', port)
    server = HTTPServer(server_address, SimpleRequestHandler)

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        server.server_close()
        server.shutdown()


if __name__ == "__main__":
    run_forever()
