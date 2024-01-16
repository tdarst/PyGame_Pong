import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()

messages = [b"Message 1 from client.", b"Message 2 from client."]

def is_server_connected(sock):
    connected = False
    try:
        sock.send(b'')
        connected = True
    except:
        print("\nServer dropped connection.\n")

    return connected



def start_connections(host, port):
    server_addr = (host, port)
    print(f"Starting connect client to {server_addr}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(server_addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    data = types.SimpleNamespace(
        msg_total=sum(len(m) for m in messages),
        recv_total=0,
        messages=messages.copy(),
        outb=b""
    )
    sel.register(sock, events, data=data)
    return sock

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            print(f"Received {recv_data!r} from server\n")
            data.recv_total += len(recv_data)
        if not recv_data or data.recv_total == data.msg_total:
            print(f"Closing client connection")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if not data.outb and data.messages:
            data.outb = data.messages.pop(0)
        if data.outb:
            print(f"Sending {data.outb!r} to client")
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]

host, port = sys.argv[1], int (sys.argv[2])
# lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# lsock.bind((host, port))

try:
    sock = start_connections(host, port)
    while True:
        if not is_server_connected(sock):
            break
        # Returns a list of tuples, one for each socket.
        # Timeout blocks until there are sockets ready for i/o
        events = sel.select()
        for key, mask in events:
            service_connection(key, mask)

except KeyboardInterrupt:
    print("exiting client")

finally:
    sel.close()
        