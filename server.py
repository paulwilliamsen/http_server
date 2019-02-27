from http.server import HTTPServer, BaseHTTPRequestHandler
from cowpy import cow
from urllib.parse import urlparse, parse_qs




class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == ('/'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            cheese = cow.Moose()
            example = cheese.milk('I am a cow this is what I say')

            self.wfile.write(f'<!DOCTYPE html><html><head><title>cowsay</title><head><body><header><nav><ul><li><a href="/cow">cowsay</a></li><ul></nav><header><main><h1>cowsay</h1><h3>Directions</h3><p>if type in the following text into the address bar.  /cow?msg= "what you want to say" <p>  <p> an example is <strong>Localhost:5000/cow?msg="I am a cow this is what I say"<strong></p><pre>{example}</pre></main></body></html>'.encode())
            return

        elif parsed_path.path == ('/cow'):
            try:
                cat = parsed_qs['msg'][0]


            except KeyError:
                self.send_response_only(400)
                self.end_headers()
                return
            cheese = cow.Moose()
            msg = cheese.milk(cat)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f'<!DOCTYPE html><html><head><title>cowsay</title><head><body><header><nav><ul><li></li><ul></nav><header><main> <pre>{msg}</pre> </main></body></html>'.encode())
            return






        # elif parsed_path.path == ('/cowxxxxx'):

        #     self.wfile.write(b'we did the thing with the qs')
        #     try:

        #         cat = parsed_qs['category'][0]
        #         self.wfile.write(b'we did the thing with the qs')
        #     except KeyError:
        #         self.send_response_only(400)
        #         self.end_headers()
        #         return

        #     self.send_response(200)
        #     self.end_headers()
        #     self.wfile.write(b'we did the thing with the qs')
        #     return
        # elif parsed_path.path == '/cow':
        #     try:
        #         cat = parsed_qs['category'][0]
        #     except KeyError:
        #         self.send_response_only(400)
        #         self.end_headers()
        #         return

            # cheese = cow.Moose()
            # msg = cheese.milk('{parsed_qs.text[0]}')

            # self.send_response(200)
            # self.send_header('Content-type', 'text/html')
            # self.end_headers()
            # self.wfile.write(f'<!DOCTYPE html><html><head><title>cowsay</title><head><body><header><nav><ul><li><a href=“/cow”>cowsay</a></li><ul></nav><header><main> <pre>{msg}</pre> project description defining how users can further interact with the application </main></body></html>'.encode())
            # return

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
