from http.server import HTTPServer, BaseHTTPRequestHandler

APP_HOST = 'localhost'
APP_PORT = 8000

class SimplGetHandler(BaseHTTPRequestHandler): 
    def _set_hendler(self): # Метод класса формирующий заголовки, которые передаются в запрос
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

    def _html(self, message): # метод класса формирующий HTML форму
        content = (
            f'<html>'
            f'<body>'
            f'<h1>{message}</h1>'
            f'</body>'
            f'</html>'
        )
        return content.encode('utf8')

    def do_GET(self): # метод, формирующий GET запрос
        self._set_hendler() # указываем заголовки которые необходимо передать в запрос (они описаны в отдельном методе класса)
        message = 'Сервер работает' # сообщение которое пердается в HTML фотму (форма описана в отдельном методе класса)
        self.wfile.write(self._html(message)) # передаем сообщение в HTML фотму (в отдельный метод класса)

def run_server(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = (APP_HOST, APP_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run_server(handler_class=SimplGetHandler)