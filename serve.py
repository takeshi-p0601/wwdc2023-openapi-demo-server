from http.server import BaseHTTPRequestHandler, HTTPServer
import random

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if '/api/emoji' in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            emojis = ['😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '😊', '😇']
            
            count_param = self.path.split("?count=")
            if len(count_param) == 2:
              count = int(count_param[1])
              random_emoji = random.choice(emojis)
              response = random_emoji * count
              self.wfile.write(response.encode())
            else:
              random_emoji = random.choice(emojis)
              response = random_emoji  # 返す文字列を指定
              self.wfile.write(response.encode())
        else:
            self.send_error(404)

server_address = ('', 8080)
httpd = HTTPServer(server_address, SimpleHandler)
httpd.serve_forever()
