import socket

"'This code snippet prints IP address of the current connection '"

hostName = socket.gethostname()

IpAddr = socket.gethostbyname(hostName)

print(IpAddr)



    
