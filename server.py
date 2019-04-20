#Server directory web for multiple requests
import http.server
import socketserver
import os

try:
  limit=int(os.environ['REQUEST_LIMIT'])
except:
  limit=0
PORT = 8000

web_dir = os.path.join(os.path.dirname(__file__), 'web')
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)

i = 1

if limit > 0:
  while i < limit:
    httpd.handle_request()
    i += 1
  httpd.socket.close()
else:
  httpd.serve_forever()