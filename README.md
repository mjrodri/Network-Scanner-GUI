# Network Scanner with GUI

## Overview

The Network Scanner with GUI is a Python application that combines the capabilities of Scapy and a socket-based port scanner to provide an intuitive graphical user interface for network reconnaissance. This tool allows users to discover devices within a specified IP range, conduct an ARP scan using Scapy, and perform a socket-based port scan to identify open ports on the target network.

## Features

- **Scapy ARP Scan:** Utilizes Scapy for an ARP scan to discover devices on the network, displaying their IP and MAC addresses.

- **Socket-based Port Scan:** Performs a basic port scan on the specified IP range using socket programming, identifying open ports.

- **Graphical User Interface (GUI):** Offers a Tkinter-based GUI for user-friendly input of IP range and easy interpretation of scan results.

## Requirements

- Python 3.x
- Scapy library (`pip install scapy`)
- Tkinter library (usually included with Python)

## Setup

1. **Install Dependencies:**
   ```bash
   pip install scapy
Clone the Repository:

bash
git clone https://github.com/your-username/network-scanner-with-gui.git
cd network-scanner-with-gui
Run the Application:

bash
python network_scanner_gui.py
Usage

Launch the application by running network_scanner_gui.py.

Enter the target IP range in the provided entry field.

Click the "Scan" button to initiate the network scan.

View the scan results in the text box, displaying information from both the Scapy ARP scan and the socket-based port scan.

Legal and Ethical Considerations
Ensure that you have the necessary permissions before scanning any network. Unauthorized scanning may violate legal and ethical standards. Use this tool responsibly and respect the privacy and security of others.

Acknowledgements
This project uses the Scapy library for ARP scanning. Scapy GitHub Repository

License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to customize the README to better fit your project's specific details a
