import socket

common_ports = {
    # Transfer
    20: "FTP-DATA",
    21: "FTP",
    69: "TFTP",
    2049: "NFS",    

    # Remote access
    22: "SSH",
    23: "Telnet",
    3389: "RDP",
    5900: "VNC",

    # Email
    25: "SMTP",
    110: "POP3",
    143: "IMAP",
    465: "SMTPS",
    587: "SMTP",
    993: "IMAPS",
    995: "POP3S",

    # DNS / DHCP
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    123: "NTP",
    161: "SNMP",
    162: "SNMP-TRAP",

    # Web
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP",
    8443: "HTTPS",
    8888: "HTTP",
    9000: "HTTP",

    # Windows
    135: "MSRPC",
    137: "NetBIOS",
    138: "NetBIOS",
    139: "NetBIOS",
    445: "SMB",
    389: "LDAP",
    636: "LDAPS",
    3268: "LDAP-GC",
    3269: "LDAPS-GC",

    # Data Base
    1433: "MSSQL",
    1521: "Oracle",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",
    27017: "MongoDB",

    # Directory/files
    111: "RPCBIND",
    2049: "NFS",

    # VoIP
    5060: "SIP",
    5061: "SIP-TLS",

    # Other common services
    5000: "HTTP/API",
    5672: "AMQP",
    9200: "Elasticsearch",
    9300: "Elasticsearch",
}

def check_ports (ip, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

def scanner_ports (ip):

    open_ports = []
    print(f"\n[*] Analyzing: {ip}")
    print("[*] Scanning ports...\n")

    for port, service in common_ports.items():

        print(f"[*] Checking {port:<5} {service:<10}", end="\r")
        if check_ports(ip, port):
            open_ports.append({ "port": port, "service": service})
    print("\n")
    return open_ports

