## Задача №3

Реализовать серверную часть приложения. Клиент подключается к серверу. 
В ответ клиент получает http-сообщение, содержащее html-страницу, 
которую сервер подгружает из файла index.html.

## Решение

1. Сервер

```

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

def load_index_page():
    with open("2_index.html", "r") as f:
        return f.read()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print('Connection address:', addr)

    data = conn.recv(BUFFER_SIZE)
    if not data: break
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + load_index_page()
    conn.send(response.encode())

conn.close()
```

## Демонстрация работы
![Веб-страница](img/3_2.png)
