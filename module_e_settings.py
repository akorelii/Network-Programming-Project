import socket

from modules.common.constants import SEND_BUF_SIZE, RECV_BUF_SIZE

def run_module_e_settings_and_errors():
    """
    Module E: Demonstrates socket settings (timeout, buffer, blocking)
    and error handling (connection, timeout).
    """
    print("\n--- Module E: Settings and Error Handling ---")

    # Socket Timeout Setting
    print("\n[PART 1: Timeout Setting]")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("  Default Timeout: %s" % s.gettimeout())
        s.settimeout(10.5)
        print("  New Timeout: %s" % s.gettimeout())
        s.close()
    except socket.error as e:
        print("  Error: %s" % e)

    # Buffer Size Setting
    print("\n[PART 2: Buffer Size Setting]")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sndbuf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        rcvbuf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
        print("  Send Buffer [Before]: %d" % sndbuf)
        print("  Receive Buffer [Before]: %d" % rcvbuf)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)

        sndbuf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        rcvbuf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
        print("  Send Buffer [After]: %d" % sndbuf)
        print("  Receive Buffer [After]: %d" % rcvbuf)
        sock.close()
    except socket.error as e:
        print("  Error: %s" % e)

    # Blocking/Non-blocking Mode Setting
    print("\n[PART 3: Blocking Mode Setting]")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("  Default Blocking Mode: %s (True=1)" % s.getblocking())
        s.setblocking(0)  # Set to non-blocking mode
        print("  New Blocking Mode: %s (False=0)" % s.getblocking())
        s.close()
    except socket.error as e:
        print("  Error: %s" % e)

    # 4: Error Handling (Connection Errors)
    print("\n[PART 4: Error Handling (Connection)]")
    # Address Error
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("www.invalid-host-name-12345.org", 80))
    except socket.gaierror as e:
        print("  SUCCESS (Error Caught): Address error -> %s" % e)
    finally:
        s.close()

    # Connection Refused Error
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost", 9999))  # Probably an empty port
    except socket.error as e:
        print("  SUCCESS (Error Caught): Connection error -> %s" % e)
    finally:
        s.close()

    # Error Handling (Timeout Error)
    print("\n[PART 5: Error Handling (Timeout)]")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        s.connect(("10.255.255.1", 80))
    except socket.timeout as e:
        print("  SUCCESS (Error Caught): Timeout error -> %s" % e)
    except socket.error as e:
        print("  SUCCESS (Error Caught): General socket error -> %s" % e)
    finally:
        s.close()

    print("\n-------------------------------------------")
