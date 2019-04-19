#Server directory web for multiple requests
import http.server
import socketserver
import os

PORT = 8000

web_dir = os.path.join(os.path.dirname(__file__), 'web')
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)

i = 0
while i < 2:
  httpd.handle_request()
  i += 1
httpd.socket.close()