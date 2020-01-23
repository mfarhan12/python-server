import socket
import time

# create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 1234))

# receive the initial message
msg = client_socket.recv(1024)
print(msg.decode("utf-8"))

# ask to do perfom Task
client_socket.send(bytes("performTask\n", "utf-8"))
time.sleep(5)

# disconnect from server
client_socket.send(bytes("disconnect\n", "utf-8"))

# close the connection
client_socket.close()
