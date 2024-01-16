import socket
import sys
import selectors
import types

def accept_wrapper(sock):
    # Accept socket connection
    conn, addr = sock.accept()
    print(f"Accepted connection from {addr}")
    # Remove blocking
    conn.setblocking(False)
    # Simple object with the given attributes
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    # Tells whether the client is ready for reading or writing
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    # Pass events mask, socket and data objects to sel.register()
    sel.register(conn, events, data=data)

sel = selectors.DefaultSelector()

host, port = sys.argv[1], int (sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()

print(f"Listening on {(host, port)}")

# Calls made to this socket are set to not block
lsock.setblocking(False)

# Registers the socket to be monitored with sel.select()
# Data keeps track of what's been sent and received on the socket.
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        # Returns a list of tuples, one for each socket.
        # Timeout blocks unti there are sockets ready for i/o
        events = sel.select(timeout=None)
        for key, mask in events:
            # If key.data is none then it's the listening socket
            # If key.data exists then it's a client socket
            if key.data is None:
                # Accept the listening socket
                accept_wrapper(key.fileobj)
            else:
                # Service the client socket
                service_connection(key, mask)

except KeyboardInterrupt:
    print("Exiting due to keyboard interrupt")
finally:
    sel.close()

def accept_wrapper(sock):
    # Accept socket connection
    conn, addr = sock.accept()
    print(f"Accepted connection from {addr}")
    # Remove blocking
    conn.setblocking(False)
    # Simple object with the given attributes
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    # Tells whether the client is ready for reading or writing
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    # Pass events mask, socket and data objects to sel.register()
    sel.register(conn, events, data=data)

# Key is the namedtuple containing the socket object and data object
# Mask contains the events that are ready.
def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
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
            sel.unregister(sock)
            sock.close()
    # If socket is ready for writing
    if mask & selectors.EVENT_WRITE:
        # If there is data to write, write it.
        if data.outb:
            print(f"Echoing {data.outb!r} to {data.addr}")
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]