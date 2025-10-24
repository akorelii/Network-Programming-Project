import socket
import sys
import threading

from modules.common.chat_utils import send, receive, log_to_file
from modules.common.constants import SERVER_HOST

class ChatClient:
    def __init__(self, name, port, host=SERVER_HOST):
        self.name = name
        self.connected = False
        self.host = host
        self.port = port
        self.prompt = f"[{name}@{socket.gethostname().split('.')[0]}]> "

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, self.port))
            print(f"Connected to chat server @ port {self.port}")
            self.connected = True
            send(self.sock, 'NAME: ' + self.name)
            data = receive(self.sock)
            addr = data.split('CLIENT: ')[1]
            self.prompt = f"[{self.name}@{addr}]> "
            log_to_file(f"--- Client ({self.name}) connected to {host}:{port} ---")
        except socket.error as e:
            print(f"Could not connect to server: {e}")
            sys.exit(1)

    # Input thread structure
    def input_thread(self):
        """Gets user input in a separate thread."""
        while self.connected:
            try:
                line = sys.stdin.readline().strip()
                if line:
                    send(self.sock, line)
                    log_to_file(f"[{self.name}]>> {line}")  #(Log outgoing message)
            except (EOFError, KeyboardInterrupt):
                self.connected = False
                break

    def run(self):
        """Client main loop. Listens for incoming messages."""
        print("Connection successful. Type your messages and press Enter.")
        print("You can use Ctrl+C to exit.")

        # Start the thread for user input
        t = threading.Thread(target=self.input_thread, daemon=True)
        t.start()

        try:
            while self.connected:
                data = receive(self.sock)
                if not data:
                    print("\nServer connection lost.")
                    self.connected = False
                else:
                    print("\n" + data)  # Incoming message
                    log_to_file(data.strip())  # (Log incoming message)
                    sys.stdout.write(self.prompt)
                    sys.stdout.flush()
        except KeyboardInterrupt:
            print("\nDisconnecting...")
        finally:
            self.connected = False
            self.sock.close()
            log_to_file(f"--- Client ({self.name}) closed the connection ---")
