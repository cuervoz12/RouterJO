import pyfiglet
import socket
import subprocess
import re
from colorama import init, Fore
from modules.network import get_information_network, get_network, get_gateway, ping_test, dns_lookup, internet_connectivity
from modules.devices import scan_devices
from modules.ports import scanner_ports
from modules.router import get_router_information

init(autoreset = True)

def view_banner ():

    print(Fore.CYAN + pyfiglet.figlet_format("RouterJO"))
    print(Fore.CYAN + "Network Analyzer v1.0")
    print()

def view_menu ():

    print(Fore.CYAN +  "╔══════════════════════════════════════════╗")
    print(Fore.CYAN +  "║                  RouterJO                ║")
    print(Fore.CYAN +  "╠══════════════════════════════════════════╣")
    print(Fore.WHITE + "║  [1]  Connected Devices                  ║")
    print(Fore.WHITE + "║  [2]  Scans Ports                        ║")
    print(Fore.WHITE + "║  [3]  Network Information                ║")
    print(Fore.WHITE + "║  [4]  Router Information                 ║")
    print(Fore.WHITE + "║  [0]  Exit                               ║")
    print(Fore.CYAN +  "╚══════════════════════════════════════════╝")


def main ():

    view_banner ()
    devices = []

    while True:

        view_menu ()

        opcion = input("\n RouterJO: ")

        if opcion == "1":
            print("\n[*] Obtaining network information....")
            name_devices = socket.gethostname()
            ip_local = socket.gethostbyname(name_devices)
            network = get_network(ip_local, "255.255.255.0")
            devices = scan_devices (network, ip_local)    

            print("========== DEVICES FOUND ==========\n")
            if devices:

                print(f"{'IP':<16}" f"{'MAC':<20}" f"{'MAKER':<30}" f"STATE")
                print("-" * 80)
                
                for device in devices:

                    print(f"[+] {device['ip']:<16}" f"{device['mac']:<20}" f"{device['maker']:<30}" f"{device['status']}")
            else:
                print("[!] No devices found.")

            print("\n==============================================")
        elif opcion == "2":
            if not devices:
                print("\n[!] No devices available.")
                print("[!] Run option 1 first.\n")
                continue

            print("\n========== SELECT DEVICE ==========\n")

            for i, device in enumerate(devices, start = 1):

                print(f"[{i}] " f"{device['ip']:<16}" f"{device['maker']:<30}")
            print("\n[0] Back")
            try:
                selected = int(input("\nSelect device: "))
            except ValueError:
                print("\n[!] Invalid option.")
                continue
            if selected == 0:
                continue
            if selected < 1 or selected > len(devices):
                print("\n[!] Invalid device.")
                continue
            device = devices[selected - 1]
            ip = device["ip"]
            print(f"\n[*] Target: {ip}")
            ports = scanner_ports(ip)

            print("\n========== OPEN PORTS ==========\n")
            if ports:

                for port in ports:

                    print(f"[+] Port: {port['port']:<6}" f"Service: {port['service']:<15}" f"OPEN")
            else:
                print("[!] No open TCP ports found.")

            print("\n================================")
        elif opcion == "3":
            while True:

                print("\n========== NETWORK INFORMATION ==========\n")

                print("[1] Network Details")
                print("[2] Ping Test")
                print("[3] DNS Lookup")
                print("[4] Internet Connectivity")
                print("[0] Back")
                network_option = input("\nNetwork Information: ")
                if network_option == "1":
                    get_information_network()
                elif network_option == "2":
                    ip = input("\nEnter IP: ").strip()
                    ping_test (ip)
                elif network_option == "3":
                    dns_lookup ()
                elif network_option == "4":
                    internet_connectivity ()
                elif network_option == "0":
                    break
                else:
                    print("\n[!] Invalid option.")
        elif opcion == "4":
            print("\n[*] Obtaining router information....")

            gateway = get_gateway()
            if gateway != "Not found":
                get_router_information(gateway)
            else:
                print("[!] Gateway not found.")
        elif opcion == "0":
            print("\n[+] Closing RouterJO...")
            break
        else:
            print("\n[!] Invalid option.")

        input("\nPress ENTER to continue...")
        print("\n")

if __name__ == "__main__":
    main ()