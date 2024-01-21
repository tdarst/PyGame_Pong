import socket

# =============================================================================
# Name: Network
# Purpose: Orchestrates all client side socket code.
# =============================================================================
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "127.0.0.1"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.id = self.connect()

    # =============================================================================
    # Name: start
    # Purpose: Connects to the server and assigns client id (which will dictate
    #          player assignment)
    # =============================================================================
    def start(self) -> None:
        self.id = self.connect()

    # =============================================================================
    # Name: connect
    # Purpose: Makes initial connection with server and receives initial server
    #          message which will be player assignment.
    # =============================================================================
    def connect(self) -> str:
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

    # =============================================================================
    # Name: send
    # Purpose: Sends local player data to the server, receives opponents data.
    # =============================================================================
    def send(self, data: str) -> str:
        try:
            self.client.send(str.encode(data))
            reply = self.client.recv(2048).decode()
        except socket.error as e:
            reply = str(e)

        return reply