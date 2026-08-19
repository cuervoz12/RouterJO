import socket
import psutil
import subprocess
import ipaddress

def network_statistics ():

    print("\n========== NETWORK STATISTICS ==========\n")

    stats = psutil.net_io_counters(pernic= True)

    for interface, data in stats.items():

        if interface == "Loopback Pseudo-Interface 1":
            continue
        print(f"Interface : {interface}")
        print("----------------------------------------")
        print(f"Bytes Sent       : {data.bytes_sent:,}")
        print(f"Bytes Received   : {data.bytes_recv:,}")
        print(f"Packets Sent     : {data.packets_sent:,}")
        print(f"Packets Received : {data.packets_recv:,}")
        print(f"Errors Sent      : {data.errout}")
        print(f"Errors Received  : {data.errin}")
        print()

    print("========================================")

def ping_test (ip):

    print("\n========== PING TEST ==========\n")

    print(f"[*] Target: {ip}\n")
    result = subprocess.run(["ping", "-n", "4", ip], capture_output= True, text= True)
    print(result.stdout)
    if result.returncode == 0:
        print("[+] Host is reachable.")
    else:
        print("[!] Host is unreachable.")
    print("\n================================")

def dns_lookup():

    print("\n========== DNS LOOKUP ==========\n")

    hostname = input("Enter hostname: ").strip()
    if not hostname:
        print("\n[!] Hostname cannot be empty.")
        print("\n================================")
        return
    if "." not in hostname:
        hostname += ".com"
    try:
        addresses = socket.getaddrinfo(hostname, None, socket.AF_UNSPEC, socket.SOCK_STREAM)
        ips = sorted(set(address[4][0] for address in addresses))
        print(f"\nHostname : {hostname}")
        print("IP Addresses:")

        for ip in ips:

            print(f"  - {ip}")
    except socket.gaierror:
        print(f"\n[!] Could not resolve: {hostname}")
    print("\n================================")

def internet_connectivity ():

    print("\n========== INTERNET TEST ==========\n")

    gateway = get_gateway ()

    if gateway:
        result = subprocess.run(["ping", "-n", "1", gateway], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            print(f"[+] Gateway ({gateway}) : OK")
        else:
            print(f"[!] Gateway ({gateway}) : FAILED")
    else:
        print("[!] Gateway : NOT FOUND")
    try:
        socket.gethostbyname("google.com")
        print("[+] DNS                  : OK")
    except socket.gaierror:
        print("[!] DNS                  : FAILED")
    result = subprocess.run(["ping", "-n", "1", "8.8.8.8"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        print("[+] Internet             : OK")
    else:
        print("[!] Internet             : FAILED")
    print("\n====================================")

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