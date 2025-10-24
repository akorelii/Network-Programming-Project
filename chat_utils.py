import socket
import pickle
import struct

from .constants import CHAT_LOG_FILE

# =============================================================================
# HELPER FUNCTION: Log to File
# Added for Module D requirement
# =============================================================================
def log_to_file(message):
    """Appends the given message to chat_log.txt."""
    try:
        with open(CHAT_LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(message + '\n')
    except IOError as e:
        print("Could not write to log file: %s" % e)

# =============================================================================
# MODULE D: Simple Chat Module
# =============================================================================

# Helper functions for chat module (send/receive)
def send(channel, *args):
    buffer = pickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L", value)
    channel.send(size)
    channel.send(buffer)


def receive(channel):
    try:
        size_data = channel.recv(struct.calcsize("L"))
        if not size_data:
            return ''
        size = socket.ntohl(struct.unpack("L", size_data)[0])
    except (struct.error, socket.error):
        return ''

    buf = b""
    while len(buf) < size:
        recv_data = channel.recv(size - len(buf))
        if not recv_data:
            return ''
        buf += recv_data
    return pickle.loads(buf)[0]

