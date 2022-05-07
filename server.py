# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65438  # Port to listen on (non-privileged ports are > 1023)


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

            if 'object' in request_obj:
                price = object_prices[request_obj]
                price_bytes = str(price).encode('utf-8')
                conn.sendall(price_bytes)

            if request_obj == 'accept':
                print('Client accepted price. Sending object now.')



                ### Payment logic: (put into a loop?)
                
                # Send object:
                conn.sendall(object_data)

                # Request money:
                payment_request = add_invoice(price)
                conn.sendall(payment_request)
