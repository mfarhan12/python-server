import socket
import time

class AdServer:
    _disconnected = False
    _shutdown = False
    _client_address = None
    _server = None
    _client_socket = None
    _PORT = 1234

    def __init__(self):

        self._start_server()

    def _start_server(self):
        # initialize the server
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind((socket.gethostname(), self._PORT))
        self._server.listen(5)
        self._listen_for_connections()

    def _listen_for_connections(self):
    
        # continuesly check for connections
        while True:
            if self._shutdown:
                break
            # listen for clients
            self._client_socket, self._client_address = self._server.accept()
            
            print(f"Connection from {self._client_address} has been established!!!")
            
            # send the client a welcome message
            self._client_socket.send(bytes("Welcome to the server", "utf-8"))
            
            # after a connection is made, listen for incoming commands
            self._listen_for_commands()

    def _listen_for_commands(self):
        # keep listening for stuff from client
        while True:
            
            # if we got disconnected, then disconnect, and go back to listening
            if self._disconnected:
                print(f"Disconnecting from {self._client_address}")
                self._disconnected = False
                self._shutdown = True
                break
            
            # listen for messages
            msg = self._client_socket.recv(1024).decode("utf-8")
            

            # if the msg has len, decode the mesage
            if len(msg) > 5:
                print("Received %s" % msg)
                self._decode_msg(msg)

    def _decode_msg(self, msg):
        
        # if the message is disconnect, then turn on disconnect flag
        if "disconnect" in msg:
            self._disconnected = True
            print("Disconnecting")
        
        elif  "performTask" in msg:
            self._perform_task()
        
        else:
            print("Cannot recognize %s", msg)

    def _perform_task(self):
        print("Performing Task")

my_server = AdServer()