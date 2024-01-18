import socket
import sys
import selectors
import types
import pickle
from classes.Base import game

class Server:
    def __init__(self):
        self.sel = selectors.DefaultSelector()

        #self.host, self.port = sys.argv[1], int (sys.argv[2])
        self.host, self.port = "127.0.0.1", 65432
        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__totalConnections = 0
        self.__totalConnectionsAllowed = 2

        self.start()

    def start(self):
        self.lsock.bind((self.host, self.port))
        self.lsock.listen()
        print(f"Listening on {(self.host, self.port)}")
        # Calls made to this socket are set to not block
        self.lsock.setblocking(False)
        # Registers the socket to be monitored with sel.select()
        # Data keeps track of what's been sent and received on the socket.
        self.sel.register(self.lsock, selectors.EVENT_READ, data=None)

    def accept_wrapper(self, sock):
        if self.connection_allowed():
            # Accept socket connection
            conn, addr = sock.accept()
            print(f"Accepted connection from {addr}")
            # Remove blocking
            conn.setblocking(False)
            # Simple object with the given attributes
            data = types.SimpleNamespace(addr=addr, 
                                         inb=b"", 
                                         outb=b"", 
                                         initConnection=True, 
                                         player=None)
            
            # Tells whether the client is ready for reading or writing
            events = selectors.EVENT_READ | selectors.EVENT_WRITE
            # Pass events mask, socket and data objects to sel.register()
            self.sel.register(conn, events, data=data)
            
            self.__totalConnections += 1
            data.player = self.__totalConnections

        else:
            conn, addr = sock.accept()
            print(f"Rejected connection from {addr}")
            conn.close()

    # Key is the namedtuple containing the socket object and data object
    # Mask contains the events that are ready.
    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data

        if data.initConnection == True:
            sock.send(str(data.player).encode())
            data.initConnection = False
        # if socket is ready for reading
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            # Save received data so it can be sent later
            if recv_data:
                data.outb += recv_data
            # If there is no data received then close the connection
            else:
                print(f"Closing connection to {data.addr}")
                # Make sure this socket is no longer monitored
                self.sel.unregister(sock)
                sock.close()
                self.__totalConnections -= 1
        # If socket is ready for writing
        if mask & selectors.EVENT_WRITE:
            # If there is data to write, write it.
            if data.outb:
                print(f"Echoing {data.outb!r} to {data.addr}")
                sent = sock.send(data.outb)
                data.outb = data.outb[sent:]

    def connection_allowed(self):
        allowed = False
        if self.__totalConnections < self.__totalConnectionsAllowed:
            allowed = True
        
        return allowed
            

    def run(self):
        running = True
        try:
            while running == True:
                # Returns a list of tuples, one for each socket.
                # Timeout blocks unti there are sockets ready for i/o
                events = self.sel.select(timeout=None)
                for key, mask in events:
                    # If key.data is none then it's the listening socket
                    # If key.data exists then it's a client socket
                    if key.data is None:
                        # Accept the listening socket
                        self.accept_wrapper(key.fileobj)
                    else:
                        # Service the client socket
                        # try:
                        #     self.service_connection(key, mask)
                        # except:
                        #     continue
                        self.service_connection(key, mask)

        except KeyboardInterrupt:
            print("Exiting due to keyboard interrupt")
        finally:
            self.sel.close()

server = Server()
server.run()