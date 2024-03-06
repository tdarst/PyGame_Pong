import socket
from _thread import *

# ======================================================================================================
# Name: setLocalControls
# Purpose: Facilitates communication between connected clients.
# ======================================================================================================
class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.serverAdd = '127.0.0.1'
        self.port = 5555

        self.server_ip = socket.gethostbyname(self.serverAdd)

        self.currentId = "0"
        self.pos = ["0:0,290", "1:795,290"]

        self.running = True

        self.initializeSocket()

    # ======================================================================================================
    # Name: initializeSocket
    # Purpose: Binds socket to address and port, and configures it for listening
    # ======================================================================================================
    def initializeSocket(self) -> None:
        try:
            self.sock.bind((self.serverAdd, self.port))

        except socket.error as e:
            print(str(e))
        
        self.sock.listen(2)
        print("Waiting for a connection")

    # ======================================================================================================
    # Name: threaded_client
    # Purpose: Threaded servicing of client connection
    # ======================================================================================================
    def threadedClient(self, conn) -> None:
        conn.send(str.encode(self.currentId))
        self.currentId = "1"
        reply = ''
        while True:
            try:
                data = conn.recv(2048)
                reply = data.decode('utf-8')
                if not data:
                    conn.send(str.encode("Goodbye"))
                    break
                else:
                    print("Recieved: " + reply)
                    arr = reply.split(":")
                    id = int(arr[0])
                    self.pos[id] = reply

                    if id == 0: nid = 1
                    if id == 1: nid = 0

                    reply = self.pos[nid][:]
                    print("Sending: " + reply)

                conn.sendall(str.encode(reply))
            except:
                break

        print("Connection Closed")
        self.running = False
        conn.close()

    # ======================================================================================================
    # Name: run
    # Purpose: Main server loop for accepting and servicing connections.
    # ======================================================================================================
    def run(self) -> None:
        try:
            while self.running:
                conn, addr = self.sock.accept()
                print("Connected to: ", addr)

                start_new_thread(self.threadedClient, (conn,))

        except KeyboardInterrupt:
            print("Exiting Server")

if __name__=="__main__":
    gameServer = Server()
    gameServer.run()

