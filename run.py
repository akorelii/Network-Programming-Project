import signal

from .server import ChatServer
from .client import ChatClient

from modules.common.constants import CHAT_LOG_FILE

def run_chat_module():
    """Module D: Lets the user choose to run as a server or client."""
    print("\n--- Module D: Simple Chat ---")
    print(f"All chat will be logged to ' {CHAT_LOG_FILE} '.")

    original_sigint_handler = signal.getsignal(signal.SIGINT)

    try:
        choice = input("Chat module: Run as (S)erver or (C)lient? ").strip().upper()

        if choice == 'S':
            port = int(input("Port to use (e.g., 8800): "))
            server = ChatServer(port)
            server.run()
        elif choice == 'C':
            name = input("Your username: ")
            port = int(input("Port to connect to (e.g., 8800): "))
            client = ChatClient(name=name, port=port)
            client.run()
        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid port number.")
    except Exception as e:
        print(f"Error in chat module: {e}")
    finally:
        signal.signal(signal.SIGINT, original_sigint_handler)
        print("\nExited chat module. Returning to main menu...")
        print("----------------------------\n")
