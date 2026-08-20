# RouterJO

<p align="center">

```text
██████╗  ██████╗ ██╗   ██╗████████╗███████╗██████╗      ██╗ ██████╗
██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗     ██║██╔═══██╗
██████╔╝██║   ██║██║   ██║   ██║   █████╗  ██████╔╝     ██║██║   ██║
██╔══██╗██║   ██║██║   ██║   ██║   ██╔══╝  ██╔══██╗██   ██║██║   ██║
██║  ██║╚██████╔╝╚██████╔╝   ██║   ███████╗██║  ██║╚█████╔╝╚██████╔╝
╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝ ╚════╝  ╚═════╝

Network Analyzer v1.0

A network analysis and diagnostic tool developed in Python.

```
</p>


## Description

**RouterJO** is a network analysis tool developed in **Python** and designed to run directly from the terminal.

The project allows you to:

-  Obtain information about the local network
-  Discover connected devices
-  Analyze TCP ports
-  Perform connectivity tests
-  Query DNS information
-  Obtain basic information about the router or network gateway

###  Project Purpose

RouterJO was developed as a learning project focused on:

- TCP/IP networking
- Python programming
- Network administration
- Connectivity diagnostics
- Automation
- Device analysis
- Ports and services
- Basic cybersecurity concepts

###  Intended Use

RouterJO is primarily intended for use on:

- Personal networks
- Virtual or physical laboratories
- Testing environments
- Networks where the user has explicit authorization to perform analysis

The tool is primarily intended for use on internal networks, in laboratories, and in environments where users have authorization to perform analyses. 

In the future, we plan to implement features to scan external networks in order to carry out brute-force attacks to obtain credentials and gain access to those networks, as well as to exploit them.


## Project Objectives

The main objectives of **RouterJO** are:

-  Learn how to work with networks using Python.
-  Retrieve information from network interfaces.
-  Detect active devices on a local network.
-  Identify device manufacturers using MAC addresses.
-  Analyze common TCP ports.
-  Perform connectivity tests.
-  Retrieve gateway and router information.
-  Practice using sockets and system commands.
-  Create a modular network analysis tool from scratch.
-  Apply basic concepts of network administration and cybersecurity.


## Features

RouterJO currently offers the following features:

```text
[1] Connected Devices
[2] Scans Ports
[3] Network Information
[4] Router Information
[6] Access Control
[0] Exit
```


## Interface

When you run RouterJO, a terminal interface appears:

```text
╔══════════════════════════════════════════╗
║                  RouterJO                ║
╠══════════════════════════════════════════╣
║  [1]  Connected Devices                  ║
║  [2]  Scans Ports                        ║
║  [3]  Network Information                ║
║  [4]  Router Information                 ║
║  [6]  Access Control                     ║
║  [0]  Exit                               ║
╚══════════════════════════════════════════╝
```


## Project Structure

The project follows a modular structure to keep the different network analysis functionalities separated:

```text
RouterJO/
│
├── main.py
├── requirements.txt
├── README.md
│
└── modules/
    │
    ├── __init__.py
    ├── network.py
    ├── devices.py
    ├── ports.py
    └── router.py

+ main.py
This is the main entry point of RouterJO.
It is responsible for:

- Starting the application.
- Displaying the application banner.
- Displaying the main menu.
- Receiving user input.
- Calling the different modules.
- Maintaining the main application flow.  

+ modules/network.py
Contains functions related to the local network.

+ modules/devices.py
Handles device discovery within the local network.

+ modules/ports.py
Contains the TCP port scanner.
It uses sockets to attempt to establish connections with different ports on the selected device.

+ modules/router.py
Contains functions related to the router or gateway.
Allows you to retrieve:

- Gateway
- MAC Address
- Manufacturer
- Status
- Latency
- Common TCP Services
```


## Libraries Used

RouterJO uses standard Python libraries and some external dependencies.

```text
# Standard Libraries

+ socket: It is used to work with network connections and TCP sockets.
It is also used to:
- Get the hostname.
- Get the local IP address.
- Resolve names.
- Check TCP services.

+ subprocess: Allows you to run operating system commands from Python. This enables you to interact with the network tools available on Windows.

+ ipaddress: Used to work with IP addresses and networks. 
It allows you to obtain a network such as: 192.xxx.x.x/00

+ re: It is Python's regular expression library.
RouterJO uses it primarily to extract:
- MAC addresses.
- IP addresses.
- Ping response times.

+ psutil: Allows you to retrieve information about network interfaces and system statistics.
It is used to view:
- Interfaces.
- IPv4 addresses.
- Subnet masks.
- Network statistics.

# External offices

PyFiglet: It is used to display the name “RouterJO” in ASCII format.
- pip install pyfiglet

Colorama: It is used to add colors to the terminal interface.
- pip install colorama


Mac Vendor Lookup: Used to try to identify the manufacturer associated with a MAC address.
- pip install mac-vendor-lookup

```


## Requirements

To run **RouterJO**, you need the following:

- **Windows**
- **Python 3.x**
- **A connection to a local network**
- **An Ethernet or Wi-Fi network adapter**
- **Windows Command Prompt**

### Network Connection

RouterJO can operate through both **Ethernet and Wi-Fi** connections.
A Wi-Fi adapter is **not required** to analyze the local network when the computer is connected via Ethernet.
However, a **Wi-Fi adapter will be required for certain future features**, such as wireless network analysis and discovery.


## Installation

### 1. Clone the Repository

Clone the RouterJO repository using Git:
```bash
git clone <REPOSITORY_URL>
```
Navigate to the project directory: cd RouterJO

### 2. Check Python

Verify that Python is installed:
```bash
python --version
```
Example:
```bash
Python 3.14.x
```
You can also use the Python launcher:
```bash
py --version
```

## Running RouterJO

Once the dependencies have been installed, run RouterJO from the project directory:
```bash
python main.py

Alternatively, you can use the Python launcher:

py main.py
```

[!IMPORTANT]
 ### Recommended Execution Order
```text
> To use all RouterJO features correctly, it is recommended to start by
> running:
>
> ```text
> [1] Connected Devices
> ```
>
> This option discovers the active devices available on the local network
> and stores the information obtained in memory.
>
> After running `[1] Connected Devices`, you can use:
>
> ```text
> [2] Scan Ports
> [6] Access Control
> ```
>
> The `[2] Scan Ports` option requires devices to be detected first using
> `[1] Connected Devices`, because you must select one of the discovered
> devices before performing the port analysis.
>
> ###  Recommended Order
>
> ```text
> 1. Connected Devices
>          ↓
> 2. Scan Ports
>          ↓
> 3. Network Information
>          ↓
> 4. Router Information
>          ↓
> 6. Access Control
> ```
>
> **Note:** `[3] Network Information` and `[4] Router Information` can be
> executed independently without running `[1] Connected Devices` first.
```