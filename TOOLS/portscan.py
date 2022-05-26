# !/usr/bin/python
# import libraries
import socket

# port list for connection
port = [21,23,25,80,110,443,8080]

for i in port:
    # Create variable for connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Defines timeout for connection
    s.settimeout(1)
    
    # closes connection
    cod = s.connect_ex(('register.br', i))

    # message of open port
    if cod == 0:
        print(i, "Open!")
    else:
        print(i, "Closed!")
