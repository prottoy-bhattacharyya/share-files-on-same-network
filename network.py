# import subprocess

# def get_ip():
#     try:
#         result = subprocess.run(["ifconfig"], capture_output=True, text=True) #for linux
#     except:
#         result = subprocess.run(["ipconfig"], capture_output=True, text=True) #for windows
    
#     return result.stdout

import socket

def get_non_loopback_ip():
    """
    Retrieves the first non-loopback IP address of the local machine.
    """
    try:
        # Get the local hostname
        local_hostname = socket.gethostname()

        # Get a list of IP addresses associated with the hostname
        # socket.gethostbyname_ex returns (hostname, aliaslist, ipaddrlist)
        ip_addresses = socket.gethostbyname_ex(local_hostname)[2]

        # Filter out loopback addresses (IPs starting with "127.")
        non_loopback_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]

        # Return the first non-loopback IP if available
        if non_loopback_ips:
            return non_loopback_ips
        else:
            return None  # No non-loopback IP found

    except socket.gaierror:
        return None  # Could not resolve hostname

