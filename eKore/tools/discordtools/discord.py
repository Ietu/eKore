import time
import datetime
import os
import subprocess
import curses
import shutil
import requests
import json
import msvcrt
import discord
import sys
import eKore
from rich.progress import Progress
from rich import align
from lolpython import lol_py 
from tqdm import tqdm
from colorama import Fore, init, Style


center = shutil.get_terminal_size().columns
pcname = (os.getenv('COMPUTERNAME'))
username = os.getlogin()

# pcname = "PCNAME"
# username = "USERNAME"

init(autoreset=True)
green = Fore.LIGHTGREEN_EX
dgreen = Fore.GREEN
white = Fore.RESET
red = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
blue = Fore.LIGHTMAGENTA_EX
dblue = Fore.MAGENTA
gray = Fore.LIGHTBLACK_EX

P = '\033[35m' # pink
G = '\033[90m' # grey
w = '\033[37m' # white
P = '\033[35m' # purple
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
RE = '\033[0m' # reset
Y = '\033[33m' # yellow
B = '\033[34m' # blue
LG = '\033[37m' # lightgrey

def discordGui():
    os.system("cls")
    print(f"""
                            {C}────────────────────────────────────────────────────{w}
                            {R}██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
                            {R}██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
                            {R}██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
                            {R}██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
                            {R}██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
                            {R}╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝
                            {C}────────────────────────────────────────────────────{w}
                                 {C}╔═══════════════════╦═══════════════════╗{w}
                                 {C}║ {w}[{R}1{w}] Main Menu     {C}║ {w}[{R}2{w}] Quit          {C}║{w}
                                 {C}╠═══════════════════╬═══════════════════╣
                                 {C}║ {w}[{R}3{w}] Spammer       {C}║ {w}[{R}4{w}] -             {C}║{w}
                                 {C}║ {w}[{R}5{w}] -             {C}║ {w}[{R}6{w}] -             {C}║{w}
                                 {C}║ {w}[{R}7{w}] -             {C}║ {w}[{R}8{w}] -             {C}║{w}
                                 {C}║ {w}[{R}9{w}] -             {C}║ {w}[{R}10{w}] -            {C}║{w}
                                 {C}║ {w}[{R}11{w}] -            {C}║ {w}[{R}12{w}] -            {C}║{w}
                                 {C}║ {w}[{R}13{w}] -            {C}║ {w}[{R}14{w}] -            {C}║{w}
                                 {C}╚═══════════════════╩═══════════════════╝{w} 
""")      

def start():
    discordGui()
    menu()

def menu():
    defaultDir = "~/Discord"
    while True:
        x = input(f"""
{C}╔═{C}({R}{pcname}{Y}㉿{R}{username}{C})-[{w}{defaultDir}{C}]
{C}╚══[{C}OPTION{C}]═> {Y}$ {RE}""")
        if x == '1':
            eKore.menu()
        elif x == '2':
            print(f"{R}Quitting...{RE}")
            time.sleep(1)
            os.system("cls")
            exit()
        elif x == '3':
            spammer()
        elif x == '4':
            break
        elif x == '5':
            break
        elif x == '6':
            print(f"{R}Exiting...")
            time.sleep(1)
            exit()
        else:
            print(f"{R}Invalid option! Please select a valid option.")
            time.sleep(1)
            os.system("cls")
            discordGui()

def spammer():
    delete = False
    while True:
        delInput = input(f"{C}> {w}Delete webhook on exit (Y/N): ")
        while delInput.capitalize() not in ["Y", "N"]:
            print("\033[F\033[K", end="")
            print(f"{R}Invalid")
            time.sleep(1.5)
            print("\033[F\033[K", end="")
            delInput = input(f"{C}> {w}Delete webhook on exit (Y/N): ")
        if delInput == "Y":
            print(f"Delete: {R}True")
            delete = True
        else:
            print(f"Delete: {R}False")
        
        url = input(f"{C}> {w}Enter webhook URL: ")
        while not url.startswith("https://discord.com/api/webhooks/"):
            print("\033[F\033[K", end="")
            print(f"{R}Invalid URL!")
            time.sleep(1.5)
            print("\033[F\033[K", end="")
            url = input(f"{C}> {w}Enter webhook URL: ")

        msg = input(f"{C}> {w}Enter message: ")
        while not msg:
            print("\033[F\033[K", end="")
            print(f"{R}Message cannot be empty!")
            time.sleep(1.5)
            print("\033[F\033[K", end="")
            msg = input(f"{C}> {w}Enter message: ")

        rate = input(f"{C}> {w}Enter rate (in seconds): ")
        while True:
            try:
                rate = float(rate)
                break
            except ValueError:
                print("\033[F\033[K", end="")
                print(f"{R}Invalid rate!")
                time.sleep(1.5)
                print("\033[F\033[K", end="")
                rate = input(f"{C}> {w}Enter rate (in seconds): ")

        cooldown = input(f"{C}> {w}Enter cooldown (in seconds): ")
        while True:
            try:
                cooldown = float(cooldown)
                break
            except ValueError:
                print("\033[F\033[K", end="")
                print(f"{R}Invalid cooldown!")
                time.sleep(1.5)
                print("\033[F\033[K", end="")
                cooldown = input(f"{C}> {w}Enter cooldown (in seconds): ")
        break

    tries = 0
    counter = 0
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    response = requests.post(url, json={"content": msg})
    print(f"\n{C}> {w}Press '{R}Q{w}' to stop.")
    print(f"{C}{current_time} {w}=> {R}[{response.status_code}] {w}Attempting to send {Y}'{msg}' {w}to '{url}' every {R}{rate} {w}seconds")
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if msvcrt.kbhit() and msvcrt.getch() == b"q":
            print(f"{R}Exiting...{RE}")
            time.sleep(2)
            start()
        response = requests.post(url, json={"content": msg})
        if response.status_code == 204:
            counter += 1
            print(f"{C}{current_time} {w}=> {R}[{response.status_code}] {w}Webhook Spammer | Sent {R}{counter} {w}messages")
            time.sleep(rate)
        elif response.status_code == 429:
            print(f"Spammer | You are being rate-limited")
            print(f"Taking a {R}{cooldown} {w}second break...")
            time.sleep(cooldown)
        elif tries != 5:
            tries += 1
            if response.status_code == 404:
                print(f"{C}{current_time} {w}=> {R}[{response.status_code}] {w}Webhook not found!")
            else:
                print(f"{C}{current_time} {w}=> {R}[{response.status_code}] {w}Request failed!")

            print(f"{C}{current_time} {w}=> {R}[{response.status_code}] {w}Reattempting...")
            time.sleep(rate)
        else:
            print("\nToo many failed attempts!\nReloading...")
            time.sleep(3.5)
            start()