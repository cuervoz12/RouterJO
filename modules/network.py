import socket
import psutil
import subprocess
import ipaddress

def get_gateway ():

    result = subprocess.run (["route", "print", "-4"], capture_output= True, text= True)
    lines = result.stdout.splitlines ()

    for line in lines:

        parts = line.split()
        if len(parts) >= 5:
            destination = parts[0]
            mask = parts[1]
            gateway = parts[2]
            if destination == "0.0.0.0" and mask == "0.0.0.0":
                return gateway
    return "Not found"

def get_network (ip_local, netmask):

    network = ipaddress.ip_network (f"{ip_local}/{netmask}", strict=False)
    return network

def get_information_network ():

    name_devices = socket.gethostname()
    ip_local = socket.gethostbyname(name_devices)
    interfaces = psutil.net_if_addrs()
    gateway = get_gateway ()
    network = get_network (ip_local, "255.255.255.0")

    print("\n========== NETWORK INFORMATION ==========\n")

    print(f"Device Name       : {name_devices}")
    print(f"IP local          : {ip_local}")
    print(f"Gateway           : {gateway}")
    print(f"Network           : {network}")

    print("\nNetwork Interfaces:")

    for interface, addresses in interfaces.items():

        for address in addresses:

            if address.family == socket.AF_INET:
                if not address.address.startswith("127."):
                    print(f"\n[{interface}]")
                    print(f"  IPv4      : {address.address}")
                    print(f"  Netmask   : {address.netmask}")
                
    print("\n========================================")