import SimpleHTTPServer
import SocketServer
import random
import time


class TestServer(SocketServer.TCPServer):
    allow_reuse_address = True


class TestRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST(self):
        n = random.randrange(1, 100)
        if n < 20:
            time.sleep(2)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    httpd = TestServer(('0.0.0.0', 8080), TestRequestHandler)
    httpd.serve_forever()
