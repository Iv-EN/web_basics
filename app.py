from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = 'localhost'
serverPort = 8081

class MyServer(BaseHTTPRequestHandler):
    """Отвечает за обработку входящих запросов."""
    filename = 'index.html'

    def get_context_data(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
           context = file.read()
        return context

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(self.get_context_data(), 'utf-8'))

if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print('Сервер запущен http://%s:%s' % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print('Сервер остановлен')