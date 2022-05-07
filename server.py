# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65437  # Port to listen on (non-privileged ports are > 1023)


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
            request_obj = conn.recv(1024).decode('utf-8')
            if not request_obj:
                break
            price = object_prices[request_obj]
            price_bytes = str(price).encode('utf-8')
            conn.sendall(price_bytes)
