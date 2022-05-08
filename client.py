# echo-client.py

import socket

import lib


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65440  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"object1")
    data = s.recv(1024).decode('utf-8')

    print(f"Received price: {data}")
    
    accept = input('Type "YES" to accept, "NO" to reject: ')
    if accept.upper() == 'YES':
        s.sendall(b"accept")
    else:
        exit(0)


    #### Payment logic: (put into a loop?)
    while True:
        # Receive object:
        data = s.recv(1024).decode('utf-8')
        print(f'Data received: {data}')
        
        # Receive payment request:
        payment_request = s.recv(1024).decode('utf-8')
        print(f'Payment request received: {payment_request}')
        
        # Pay invoice
        confirmation = lib.pay_invoice(payment_request)
        print(f'Invoice paid: {confirmation}')
        

