import sys
import socket
import selectors
import types

class Client:
    def __init__(self):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sel = selectors.DefaultSelector()
        self.host, self.port = sys.argv[1], int(sys.argv[2])
        self.messages = [b"Message 1 from client.", b"Message 2 from client."]

        self.start()

    def is_server_connected(self, sock):
        connected = False
        try:
            sock.send(b'')
            connected = True
        except:
            print("\nServer dropped connection.\n")
        return connected



    def start(self):
        server_addr = (self.host, self.port)
        print(f"Starting connect client to {server_addr}")
        self.sock.setblocking(False)
        self.sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(
            msg_total=sum(len(m) for m in self.messages),
            recv_total=0,
            messages=self.messages.copy(),
            outb=b""
        )
        self.sel.register(self.sock, events, data=data)

    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                print(f"Received {recv_data!r} from server\n")
                data.recv_total += len(recv_data)
            if not recv_data or data.recv_total == data.msg_total:
                print(f"Closing client connection")
                self.sel.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if not data.outb and data.messages:
                data.outb = data.messages.pop(0)
            if data.outb:
                print(f"Sending {data.outb!r} to client")
                sent = sock.send(data.outb)
                data.outb = data.outb[sent:]

    def run(self):
        try:

            while True:
                if not self.is_server_connected(self.sock):
                    break
                # Returns a list of tuples, one for each socket.
                # Timeout blocks until there are sockets ready for i/o
                events = self.sel.select()
                for key, mask in events:
                    self.service_connection(key, mask)

        except KeyboardInterrupt:
            print("exiting client")

        finally:
            self.sel.close()

client = Client()
client.run()
        