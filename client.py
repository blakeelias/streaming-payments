# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65438  # The port used by the server

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
        
    # Receive data:
    data = s.recv(1024).decode('utf-8')
        
    # Receive payment request:
    payment_request = s.recv(1024).decode('utf-8')

    # Pay invoice
    lib.pay_invoice(payment_request)

        
print(f"Received price: {data}")
