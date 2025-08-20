#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import network


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'share_files.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    local_ips = network.get_non_loopback_ip()
    print("local Host -> http://127.0.0.1:8000")
    
    
    if local_ips:
        if len(local_ips) > 1:
            print("One of these address will work: \n")
        for ip in local_ips:
            print(f"Network IP -> http://{ip}:8000")
    else:
        print("No Network IP Found\n")
    
    print("\n")
    main()
    
