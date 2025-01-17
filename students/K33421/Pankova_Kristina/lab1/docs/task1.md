## Задача №1

Реализовать клиентскую и серверную часть приложения. Клиент отсылает 
серверу сообщение “Hello, server”. Сообщение должно отразиться на 
сервере.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение 
должно отобразиться у клиента.
Обязательно использовать библиотеку socket.
Реализовать с использованием протокола UDP.

## Решение

1. Сервер

```
import socket

HOST = '127.0.0.1'  # Локальный адрес
PORT = 65432        # Выбранный порт

# Создаем сокет
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))    # Привязываем сокет к адресу и порту
    print('Server started...')
    while True:
        data, addr = s.recvfrom(1024)  # Получаем данные от клиента
        print('Received from client:', data.decode())
        s.sendto(b'Hello, client', addr)  # Отправляем ответ клиенту
```

2. Клиент

```
import socket

HOST = '127.0.0.1'  # Локальный адрес сервера
PORT = 65432        # Выбранный порт

# Создаем сокет и подключаемся к серверу
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'Hello, server', (HOST, PORT))  # Отправляем сообщение серверу
    data, addr = s.recvfrom(1024)         # Получаем ответ от сервера
    print('Received from server:', data.decode())
```

## Пример работы программы

![Серверная часть](img/1.png)
![Клиентская часть](img/2.png)