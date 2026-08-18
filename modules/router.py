import subprocess
import re
from mac_vendor_lookup import MacLookup

mack_lookup = MacLookup()

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
    result =  subprocess.run(["ping", "-n", "1", "-w", "500", gateway], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        print("Response       : ONLINE")
    else:
        print("Response       : OFFLINE")

    print("\n========================================")