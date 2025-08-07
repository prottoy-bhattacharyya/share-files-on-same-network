import subprocess
import re
import platform

def get_ip_and_dns_suffix():
    """
    Retrieves IP addresses and their connection-specific DNS suffixes
    by parsing the output of 'ipconfig /all' on Windows.
    """
    if platform.system() != "Windows":
        print("This program is designed for Windows operating systems.")
        print("For Linux/macOS, you would typically look at 'ip addr' and '/etc/resolv.conf'")
        print("or use tools like 'nmcli' or 'ifconfig' (deprecated).")
        return

    try:
        # Execute ipconfig /all command
        # The 'text=True' argument ensures the output is decoded as a string
        # The 'encoding="cp850"' is often necessary for ipconfig output on some Windows systems
        # If you see decoding errors, try 'encoding="utf-8"' or remove the encoding argument
        result = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True, encoding="cp850", check=True)
        output = result.stdout
    except FileNotFoundError:
        print("Error: 'ipconfig' command not found. Are you on a Windows system?")
        return
    except subprocess.CalledProcessError as e:
        print(f"Error executing 'ipconfig /all': {e}")
        print(f"Stderr: {e.stderr}")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Regular expressions to find the relevant information
    # Finds adapter names like "Ethernet adapter Ethernet:" or "Wireless LAN adapter Wi-Fi:"
    adapter_name_pattern = re.compile(r"^\s*([A-Za-z0-9\s-]+(?:adapter|Adapter)\s[A-Za-z0-9\s-]+):", re.MULTILINE)
    # Finds IPv4 Address
    ipv4_pattern = re.compile(r"IPv4 Address[.\s]+:\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    # Finds Connection-specific DNS Suffix
    dns_suffix_pattern = re.compile(r"Connection-specific DNS Suffix[.\s]+:\s*([^\s]+)")

    adapters_info = []
    current_adapter = {}

    # Split the output into sections based on adapter names
    # This helps in associating details with the correct adapter
    sections = adapter_name_pattern.split(output)

    # The first element of sections will be everything before the first adapter, which we can ignore
    # We iterate through pairs: (adapter_name, adapter_details_string)
    for i in range(1, len(sections), 2):
        adapter_name = sections[i].strip()
        adapter_details = sections[i+1]

        # Reset for the new adapter
        current_adapter = {
            "name": adapter_name,
            "ipv4_address": "N/A",
            "dns_suffix": "N/A"
        }

        # Search for IPv4 address within this adapter's details
        ipv4_match = ipv4_pattern.search(adapter_details)
        if ipv4_match:
            current_adapter["ipv4_address"] = ipv4_match.group(1)

        # Search for DNS suffix within this adapter's details
        dns_suffix_match = dns_suffix_pattern.search(adapter_details)
        if dns_suffix_match:
            current_adapter["dns_suffix"] = dns_suffix_match.group(1)

        adapters_info.append(current_adapter)

    if adapters_info:
        for adapter in adapters_info:
            if adapter['dns_suffix'] == "Home":
                return adapter['ipv4_address']
            