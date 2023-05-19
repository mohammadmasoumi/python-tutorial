# echo-client.py

import socket

# localhost
# HOST = "localhost"
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

client_name = "ASGHAR: "


def receiver(s):
    data = s.recv(1024)
    print(f"{client_name}: {data.decode()}")


def sender(s):
    msg = input('ME: ')
    s.sendall(msg.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()  # start run
    conn, addr = s.accept()  # accept connection

    with conn:
        print(f"Connected by {addr}")

        while True:
            sender(conn)
            receiver(conn)
