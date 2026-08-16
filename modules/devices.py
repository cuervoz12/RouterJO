import subprocess
import ipaddress
import re 
from mac_vendor_lookup import MacLookup

mack_lookup = MacLookup()

def get_maker (mac):

    if mac == "Unknown":
        return "Unknown"
    try:
        maker = mack_lookup.lookup(mac)
        return maker
    except Exception:
        return "Unkown"

def ping_ip (ip):

    subprocess.run (["ping", "-n", "1", "-w", "300", str(ip)], stdout= subprocess.DEVNULL, stderr= subprocess.DEVNULL)

def get_arp_table ():

    result = subprocess.run(["arp", "-a"], capture_output= True, text= True)
    return result.stdout
    

def scan_devices (network, local_ip):

    devices = []
    devices.append({ "ip": local_ip, "mac": "LOCAL", "maker": "This PC", "status": "ACTIVE"})
    print("\n[*] Scanning Network...")
    print(f"[*] Target network: {network}\n")

    for ip in network.hosts():

        print(f"[*] Checking {ip}...", end="\r")
        ping_ip (ip)
    print("\n[*] Reading ARP table...\n")
    arp_table = get_arp_table ()
    pattern = re.compile(r"(\d{1,3}(?:\.\d{1,3}){3})\s+" r"([0-9a-fA-F]{2}(?:-[0-9a-fA-F]{2}){5})\s+" r"(\w+)")

    for coincidence in pattern.finditer(arp_table):

        ip = coincidence.group(1)
        mac = coincidence.group(2)
        if mac.lower() == "ff-ff-ff-ff-ff-ff":
            continue
        if ip not in [str(host) for host in network.hosts()]:
            continue
        maker = get_maker (mac)
        devices.append({ "ip": ip, "mac": mac, "maker": maker, "status": "ACTIVE" })


    return devices
