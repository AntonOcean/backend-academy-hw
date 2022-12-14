import socket


def listen():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('0.0.0.0', 5555))
    connection.listen(10)
    while True:
        current_connection, address = connection.accept()
        while True:
            data = current_connection.recv(1)
            print(f"i catch data: {data}")
            if data == b'quit\n':
                current_connection.shutdown(1)
                current_connection.close()
                break
            elif data == b'stop\n':
                current_connection.shutdown(1)
                current_connection.close()
                return
            elif data:
                current_connection.send(data.upper())

print("I start")
listen()
print("I finish")