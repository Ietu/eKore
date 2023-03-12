import socket
import threading
import math
import subprocess
import time
import sys
import os
from tools.networktools import networkmenu
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import Value
from datetime import datetime

pcname = (os.getenv('COMPUTERNAME'))
username = os.getlogin()

P = '\033[35m' # pink
G1 = '\033[90m' # grey
w = '\033[37m' # white
P = '\033[35m' # purple
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
RE = '\033[0m' # reset
Y = '\033[33m' # yellow
B = '\033[34m' # blue
LG = '\033[37m' # lightgrey

# TODO: PRINT ALWAYS WHEN OPEN PORT FOUND AFTER EG. 
# Scanning Progress: 88.89%  | Currently scanned: 8/9 ports | Open ports found: 3

# TODO: MORE FEATURES
# Host discovery — probing by IP address and providing information on the systems that respond
# Port scanning — identifying services that are available for use
# Version detection — identifying applications and their versions
# OS detection — determining the operating system along with some hardware characteristics


# def banner():
#     print('''
      
# $$$$$$$\                       $$\                                                                      
# $$  __$$\                      $$ |                                                                     
# $$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\          $$$$$$$\  $$$$$$$\ $$$$$$\  $$$$$$$\  $$$$$$$\ $$$$$$\   $$$$$$\ 
# $$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|        $$  _____|$$  _____|\____$$\ $$  __$$\ $$  __$$\$$  __$$\ $$  __$$\ 
# $$  ____/ $$ /  $$ |$$ |  \__| $$ |          \$$$$$$\  $$ /      $$$$$$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
# $$ |      $$ |  $$ |$$ |       $$ |$$\        \____$$\ $$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |       
# $$ |      \$$$$$$  |$$ |       \$$$$  |      $$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |$$ |  $$ |\$$$$$$$\ $$ |      
# \__|       \______/ \__|        \____/       \_______/  \_______|\_______|\__|  \__|\__|  \__| \_______|\__|
# |                                                                                                          |
# |----------------------------------------------------------------------------------------------------------|''')

def clear():
# for windows
    if os.name == 'nt':
        _ = os.system('cls')
# for mac and linux
    else:
        _ = os.system('clear')
clear()

def input_print():
    defaultDir = "~/Network"
    x = input(f"""
{C}╔═{C}({R}{pcname}{Y}㉿{R}{username}{C})-[{w}{defaultDir}{C}]
{C}╚══[{B}OPTION{C}]═> {Y}$ {RE}""")
    return x

def get_Host_name_IP(host):
    try:
        host_name = socket.gethostbyaddr(host)
        print(f"{C}> {w}Hostname: {host_name}")
    except:
        print(f"{C}> {w}Unable to get Hostname and IP")

def get_host_info(host):
    try:
        hostname = socket.gethostbyaddr(host)[0]
    except: 
        print(f"{C}> {w}Unable to get information")

    try:
        response = os.system("ping -n 1 " + host)
    except Exception as e:
        print(f"{C}> {w}Error Occured: {e}")
    if response == 0:
        print(f"\n{C}> {w}Host: {host} is up!\n")
        print(f"{C}> {w}Hostname: {hostname}")
    else:
        print(f"\n{C}> {w}Host: {host} is down!\n")


def progressBar(progress, total):
    progress + 1
    percent = 100 * (progress / float(total))
    bar = '█' * math.floor(percent) +  '-' * (100 - math.floor(percent))
    if percent == 100:
        print(f"|{bar}| {percent:.2f}%")
    else:
        print(f"|{bar}| {percent:.2f}%", end = "\r")


def ping_scan(ip_address):
    ip_parts = ip_address.rsplit(".", 1)
    ip_address = ip_parts[0]
    for i in range(1, 255):
        host = ip_address + "." + str(i)
        ping_response = subprocess.run(['ping', '-n', '1', '-w', '500', host], stdout=subprocess.PIPE)
        if ping_response.returncode == 0:
            print(ip_address + " is up!")
            arp_output = subprocess.run(["arp", host], stdout=subprocess.PIPE).stdout.decode()
            mac_address = arp_output.split()[3]
            manufacturer = get_manufacturer(mac_address)
            print(f"{host} is reachable. MAC: {mac_address} Manufacturer: {manufacturer}")
        else:
            print(f"{host} is not reachable.")
        
def ping_subnet(subnet):
    arp_output = subprocess.run(["arp", "-a"], stdout=subprocess.PIPE).stdout.decode()
    for line in arp_output.split("\n"):
        if subnet in line:
            ip_address = line.split()[1].strip("(")[:-1]
            mac_address = line.split()[3]
            manufacturer = get_manufacturer(mac_address)
            print(f"{ip_address} has MAC: {mac_address} Manufacturer: {manufacturer}")
current_port = 0
lock = threading.Lock()
print_lock = threading.Lock()

def thread_scan(host, start_port, end_port, open_ports, progress, current_port, thread_count):
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.2)
        try:
            result = s.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
            s.close()
        except socket.gaierror:
            pass
        current_port.value += 1
        progress.value = (current_port.value / (end_port - start_port + 1) * 100) / thread_count
        print(f"\rScanning Progress: {progress.value:.2f}%", end="")
    return

def scanOption(host, start_port, end_port):
    current_port = Value('i', 0)
    open_ports = []
    progress = Value('f', 0)
    thread_count = int(input(f"{C}> {w}Enter the number of threads to use: "))
    try:
        addr = socket.getaddrinfo(host, None)[0][4][0]
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"{C}> {w}Starting a scan on: {R}{host} {w}at {R}{dt_string}")
    except socket.gaierror as e:
        print(f"{C}> {R}Error Occured: {e}")
        return
    get_Host_name_IP(addr)
    chunk_size = (end_port - start_port + 1) // thread_count
    threads = []
    for i in range(thread_count):
        start = start_port + i * chunk_size
        end = start_port + (i + 1) * chunk_size - 1
        if i == thread_count - 1:
            end = end_port
        t = threading.Thread(target=thread_scan, args=(
            host, start, end, open_ports, progress, current_port, thread_count))
        threads.append(t)
        t.start()

    total_ports = end_port - start_port + 1

    for t in threads:
        t.join()
    if current_port.value == total_ports:
        print(f"\n{C}> {w}Scanning Progress: Done!")
        print(f"\n{C}> {w}Amount of open ports: {len(open_ports)}")
        save_to_file = input(
            f"{C}> {w}Do you want to save the open ports to a txt file? (Y/N): ")
        if save_to_file.lower() == 'y':
            with open('open_ports.txt', 'w') as f:
                f.write('\n'.join(map(str, open_ports)))
            print(f"{C}> {w}Open ports saved to open_ports.txt")
            sys.stdout.flush()
            input()
            main()
        else:
            print(f"{C}> {w}Open ports on {host}: {open_ports}")
            print(f"{C}> {w}Press '{R}Enter{RE}' to continue.")
            sys.stdout.flush()
            input()
            main()

def host_discovery(host):
    start_ip = host.split(".")[:-1]
    start_ip.append("1")
    start_ip = ".".join(start_ip)
    end_ip = host.split(".")[:-1]
    end_ip.append("255")
    end_ip = ".".join(end_ip)
    print(f"Scanning IP addresses from {start_ip} to {end_ip}")
    for ip in range(int(start_ip.split(".")[-1]), int(end_ip.split(".")[-1])+1):
        ip_address = f"{start_ip.split('.')[0]}.{start_ip.split('.')[1]}.{start_ip.split('.')[2]}.{ip}"
        print(f"{C}> {w}CURRENT: {ip_address}")
        try:
            host_name = socket.gethostbyaddr(ip_address)[0]
            print(f"{ip_address} - {host_name}")
        except socket.herror:
            pass

def invalidOption():
    for i in range(3):
        print(f"{R}Invalid option!{RE}", end="\r")
        time.sleep(0.5)
        sys.stdout.write('\033[2K\r')
        time.sleep(0.5)


def main():
    networkmenu.nworkGui()
    #print("\033[F\033[F", end="")
    print(f"{C}> {w}'1' for Port Scan  {C}| {w}'2' for Host Discovery")
    print(f"{C}> {w}'3' for Ping Sweep {C}| {w}'4' Back to menu")
    print("\033[F", end="")
    option = input_print()
    if option == "1":
        try:
            host = input(f"{C}> {w}Enter the ip/domain to scan: ")
            option == 0
            print(f"Current target: {R}[{w}{host}{R}]{RE}")
            print(f"{C}> {w}1 for Most common ports")
            print(f"{C}> {w}2 for Custom port range")
            print(f"{C}> {w}3 for Single ports")
            print(f"{C}> {w}4 to go back")
            option2 = input(f"{C}> {w}Enter mode: ")
            if option2 == "1":
                print(f"{C}> {w}Most common ports")
            elif option2 == "2":
                start_port = int(input(f"{C}> {w}Enter start port: "))
                end_port = int(input(f"{C}> {w}Enter end port: "))
                scanOption(host, start_port, end_port)
            elif option2 == "3":
                start_port = int(input(f"{C}> {w}Enter port: "))
                end_port = start_port
                scanOption(host, start_port, end_port)
            elif option2 == "4":
                option == 0
                option2 == 0
                time.sleep()
                main()
            else:
                invalidOption()
                time.sleep(1)
                main()
        except:
            main()
    
    elif option == "2":
        network_range = input(f"{C}> {w}Enter network range(eg: 192.168.1.0/24): ")
        host_discovery(network_range)
        return
    elif option == "3":
        ip = input(f"{C}> {w}Enter ip (eg: 192.168.1.0): ")
        ping_scan(ip)
        print(f"Press '{R}Enter{RE}' to exit.")
        input()
    elif option == "4":
        print(f"{R}Exiting...{RE}")
        networkmenu.start()
    else:
        invalidOption()
        main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")