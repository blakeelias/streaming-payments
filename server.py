# echo-server.py

import socket

import lib


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65440  # Port to listen on (non-privileged ports are > 1023)


object_prices = {
    'object1': 10,
    'object2': 20,
}

object_data = {
    'object1': 'object1 data',
    'object2': 'object2 data',
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        #### Initial handshake

        # (1): Determine which object the consumer wants
        request_obj = conn.recv(1024).decode('utf-8')

        if not request_obj:
            exit(0)

        if request_obj not in object_prices:
            print('Invalid object requested')

        # (2): Send price to consumer:
        price = object_prices[request_obj]
        price_bytes = str(price).encode('utf-8')
        conn.sendall(price_bytes)


        # (3): Wait for acceptance:
        accept_obj = conn.recv(1024).decode('utf-8')
        
        if accept_obj == 'accept':
            print('Client accepted price. Begin sending object stream now.')
        else:
            print('Client rejected price.')
            exit(0)
            
        #### Main streaming loop
        while True:
            # Send object:
            print(f'Sending object: {object_data[request_obj]}')
            conn.sendall(object_data[request_obj].encode('utf-8'))

            # Request money:
            payment_request = lib.add_invoice(price)
            print(f'Sent payment request: {payment_request}')
            conn.sendall(payment_request.encode('utf-8'))

            # TODO: block until money received
