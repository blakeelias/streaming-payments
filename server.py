# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


object_prices = {
    'object1': 10,
    'object2': 20,
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            request = conn.recv(1024)
            if not request:
                break
            price = object_prices[request_obj]
            conn.sendall(price)
