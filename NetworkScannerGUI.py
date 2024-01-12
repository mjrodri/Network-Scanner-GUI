import tkinter as tk
from tkinter import ttk
import socket
import scapy.all as scapy
import subprocess

class NetworkScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Scanner")

        self.create_widgets()

    def create_widgets(self):
        # IP Address Entry
        self.ip_label = ttk.Label(self.root, text="Enter IP Range:")
        self.ip_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.ip_entry = ttk.Entry(self.root)
        self.ip_entry.grid(row=0, column=1, padx=10, pady=10)

        # Scan Buttons
        self.scan_button = ttk.Button(self.root, text="Scan", command=self.scan_network)
        self.scan_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Results Textbox
        self.results_text = tk.Text(self.root, height=10, width=50)
        self.results_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def scan_ports(self, target, start_port, end_port):
        open_ports = []

        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)

            sock.close()

        return open_ports

    def scan_network(self):
        target_ip = self.ip_entry.get()

        # Scapy ARP Scan
        arp_scan_result = self.scapy_scan(target_ip)
        self.results_text.insert(tk.END, "Scapy ARP Scan Results:\n")
        self.results_text.insert(tk.END, arp_scan_result)
        self.results_text.insert(tk.END, "\n\n")

        # Socket-based Port Scan
        port_scan_result = self.scan_ports(target_ip, 1, 1024)
        self.results_text.insert(tk.END, "Socket-based Port Scan Results:\n")
        if port_scan_result:
            self.results_text.insert(tk.END, f"Open ports: {', '.join(map(str, port_scan_result))}\n")
        else:
            self.results_text.insert(tk.END, "No open ports found.\n")

    def scapy_scan(self, ip):
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        clients_list = []
        for element in answered_list:
            client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
            clients_list.append(client_dict)

        result_str = ""
        for client in clients_list:
            result_str += f"IP Address: {client['ip']}\tMAC Address: {client['mac']}\n"

        return result_str

def main():
    root = tk.Tk()
    app = NetworkScannerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()