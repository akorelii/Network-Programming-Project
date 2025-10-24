import socket
import select
import signal

from modules.common.chat_utils import send, receive, log_to_file
from modules.common.constants import SERVER_HOST

class ChatServer:
    def __init__(self, port, backlog=5):
        self.clients = 0
        self.clientmap = {}
        self.outputs = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((SERVER_HOST, port))
        print(f"Chat Server listening on {SERVER_HOST}:{port}...")
        print("(Press Ctrl+C to stop listening and return to the main menu.)")
        log_to_file(f"--- Server started on {SERVER_HOST}:{port} ---")
        self.server.listen(backlog)
        signal.signal(signal.SIGINT, self.sighandler)

    def sighandler(self, signum, frame):
        print("Shutting down server...")
        log_to_file("--- Server shut down ---")
        for output in self.outputs:
            output.close()
        self.server.close()

    def get_client_name(self, client):
        info = self.clientmap[client]
        host, name = info[0][0], info[1]
        return '@'.join((name, host))

    def run(self):
        inputs = [self.server]
        self.outputs = []
        running = True
        while running:
            try:
                readable, _, _ = select.select(inputs, self.outputs, [])
            except select.error:
                break

            for sock in readable:
                if sock == self.server:
                    client, address = self.server.accept()
                    print(f"New connection: {client.fileno()} from {address}")
                    cname = receive(client).split('NAME: ')[1]
                    self.clients += 1
                    send(client, 'CLIENT: ' + str(address[0]))
                    inputs.append(client)
                    self.clientmap[client] = (address, cname)

                    msg = f"\n(Connected: New client ({self.clients}) from {self.get_client_name(client)})"
                    log_to_file(msg.strip())
                    for output in self.outputs:
                        send(output, msg)
                    self.outputs.append(client)
                else:
                    try:
                        data = receive(sock)
                        if data:
                            msg = f"\n#[{self.get_client_name(sock)}]>> {data}"
                            print(msg.strip())
                            log_to_file(msg.strip())
                            for output in self.outputs:
                                if output != sock:
                                    send(output, msg)
                        else:
                            client_name = self.get_client_name(sock)
                            print(f"Client connection lost: {sock.fileno()}")
                            msg = f"\n(Disconnected: {client_name})"
                            log_to_file(msg.strip())
                            self.clients -= 1
                            sock.close()
                            inputs.remove(sock)
                            self.outputs.remove(sock)
                            for output in self.outputs:
                                send(output, msg)
                    except socket.error:
                        sock.close()
                        inputs.remove(sock)
                        self.outputs.remove(sock)
