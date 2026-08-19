import subprocess
import re
import socket
from mac_vendor_lookup import MacLookup

mack_lookup = MacLookup()

def check_router_port (gateway, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((gateway, port))
    sock.close()
    return result == 0

def get_router_services (gateway):

    services = {
        53: "DNS",
        80: "HTTP",
        443: "HTTPS",
        8080: "HTTP-ALT",
        8443: "HTTPS-ALT"
    }

    print("\nSERVICES")
    print("----------------------------------------")

    for port, service in services.items():

        if check_router_port(gateway, port):
            print(f"[+] {port:<6} {service:<12} OPEN")
        else:
            print(f"[-] {port:<6} {service:<12} CLOSED")

def get_router_mac (gateway):

    result = subprocess.run(["arp", "-a", gateway], capture_output=True, text=True)
    pattern = r"([0-9a-fA-F]{2}(?:-[0-9a-fA-F]{2}){5})"
    match = re.search(pattern, result.stdout)
    if match:
        return match.group(1)
    return "Unknown"

def get_router_maker (mac):

    if mac == "Unknown":
        return "Unknown"
    try:
        return mack_lookup.lookup(mac)
    except Exception:
        return "Unknown"

def get_router_information (gateway):

    print("\n========== ROUTER INFORMATION ==========\n")

    print(f"Gateway        : {gateway}")
    mac = get_router_mac (gateway)
    print(f"MAC Address    : {mac}")
    maker = get_router_maker(mac)
    print(f"Maker          : {maker}")
    result = subprocess.run(["ping", "-n", "1", "-w", "500", gateway], capture_output=True, text=True)
    if result.returncode == 0:
        print("Response       : ONLINE")
        match = re.search(r"time[=<](\d+)ms", result.stdout)
        if match:
            print(f"Latency        : {match.group(1)} ms")
        else:
            print("Latency        : <1 ms")
    else:
        print("Response       : OFFLINE")
        print("Latency        : N/A")
    get_router_services (gateway)
    print("\n========================================")