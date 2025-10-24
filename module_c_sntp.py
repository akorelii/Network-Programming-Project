import ntplib
from time import ctime

# =============================================================================
# MODULE C: SNTP Time Synchronization Module
# =============================================================================
def run_sntp_check():
    """Module C: Retrieves and prints time from an SNTP server."""
    print("\n--- Module C: SNTP Time Check ---")
    try:
        ntp_client = ntplib.NTPClient()
        response = ntp_client.request('pool.ntp.org')
        server_time = ctime(response.tx_time)
        print("Time Received from SNTP Server: %s" % server_time)
    except Exception as e:
        print("Error while getting SNTP time: %s" % e)
    print("------------------------------------\n")
