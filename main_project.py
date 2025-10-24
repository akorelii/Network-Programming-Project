import sys
import signal

from modules.module_a_info import run_machine_info
from modules.module_b_echo.run import run_echo_test
from modules.module_c_sntp import run_sntp_check
from modules.module_d_chat.run import run_chat_module
from modules.module_e_settings import run_module_e_settings_and_errors

def main_menu():
    """
    Interactive main menu that asks the user which module to run.
    """
    # For safe exit with Ctrl+C
    def signal_handler_main(sig, frame):
        print('\nExiting program. Goodbye!')
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler_main)

    while True:
        print("\n=============================================")
        print("  CEN322 - NETWORK PROGRAMMING PROJECT      ")
        print("  Network Diagnostic and Tool Package       ")
        print("  2020556041-Ahmet Can Köreli      ")
        print("=============================================")
        print("Please select the module you want to run:")
        print("  1. Module A: Show Machine Info")
        print("  2. Module B: Run Echo Test")
        print("  3. Module C: Perform SNTP Time Check")
        print("  4. Module D: Start Simple Chat Module")
        print("  5. Module E: Settings and Error Handling Demo")
        print("  6. Exit")
        print("---------------------------------------------")

        choice = input("Your choice (1-6): ").strip()

        if choice == '1':
            run_machine_info()
        elif choice == '2':
            run_echo_test()
        elif choice == '3':
            run_sntp_check()
        elif choice == '4':
            run_chat_module()
        elif choice == '5':
            run_module_e_settings_and_errors()
        elif choice == '6':
            print("Exiting program...")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

        input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    main_menu()