import socket


def run_machine_info():
    """
    Module A: Prints the local machine's hostname and
    associated IP interfaces.
    """
    print("\n--- Module A: Machine Info ---")
    try:
        host_name = socket.gethostname()
        print("Hostname: %s" % host_name)

        (hostname, aliases, ip_addresses) = socket.gethostbyname_ex(host_name)
        print("  Hostname: %s" % hostname)
        print("  Interface IP Addresses:")
        for ip in ip_addresses:
            print("    - %s" % ip)

    except socket.error as e:
        print("Error occurred while getting machine info: %s" % e)
    print("---------------------------------\n")