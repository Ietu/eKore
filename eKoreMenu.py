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
from rich.progress import Progress
from rich import align
from lolpython import lol_py 
from tqdm import tqdm
from colorama import Fore, init, Style

os.system("cls")

center = shutil.get_terminal_size().columns
pcname = (os.getenv('COMPUTERNAME'))
username = os.getlogin()


init(autoreset=True)
green = Fore.LIGHTGREEN_EX
dgreen = Fore.GREEN
white = Fore.RESET
red = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
blue = Fore.LIGHTMAGENTA_EX
dblue = Fore.MAGENTA
gray = Fore.LIGHTBLACK_EX
intents = discord.Intents.all()

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

def start():
    os.system('cls')
    curses.wrapper(scrollText)
    gui()
    menu()

def scrollText(stdscr):
    message = f"Logging in as {username}: "
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    x = width // 2 - len(message) // 2
    y = height // 2
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_CYAN, -1) 
    curses.init_pair(2, curses.COLOR_RED, -1)
    stdscr.border()
    for i, char in enumerate(message + pcname):
        if i >= width-1:
            break
        stdscr.addstr(y, x + i, char, curses.color_pair(1))
        stdscr.refresh()
        time.sleep(0.1)
    time.sleep(1)

def gui():
    os.system("cls")
    print(f"""
                                {B}────────────────────────────────────────{w}
                                {C}███████╗██╗  ██╗ ██████╗ ██████╗ ███████╗
                                {C}██╔════╝██║ ██╔╝██╔═══██╗██╔══██╗██╔════╝
                                {C}█████╗  █████╔╝ ██║   ██║██████╔╝█████╗  
                                {C}██╔══╝  ██╔═██╗ ██║   ██║██╔══██╗██╔══╝  
                                {C}███████╗██║  ██╗╚██████╔╝██║  ██║███████╗
                                {C}╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝            
                                {B}────────────────────────────────────────{w}
                                 {B}╔══════════════════╦═════════════════╗{w}
                                 {B}║ {w}[{C}1{w}] Show sys info{B}║ {w}[{C}2{w}] -           {B}║{w}
                                 {B}║ {w}[{C}3{w}] Discord      {B}║ {w}[{C}4{w}] -           {B}║{w}
                                 {B}║ {w}[{C}5{w}] -            {B}║ {w}[{C}6{w}] -           {B}║{w}
                                 {B}║ {w}[{C}7{w}] -            {B}║ {w}[{C}8{w}] -           {B}║{w}
                                 {B}║ {w}[{C}9{w}] -            {B}║ {w}[{C}10{w}] -          {B}║{w}
                                 {B}║ {w}[{C}11{w}] -           {B}║ {w}[{C}12{w}] -          {B}║{w}
                                 {B}║ {w}[{C}13{w}] -           {B}║ {w}[{C}14{w}] -          {B}║{w}
                                 {B}╚══════════════════╩═════════════════╝{w} 
""")      
    
def menu():
    gui()
    while True:
        x = input(f"""
{B}╔═{B}[{C}{pcname}{Y}@{C}{username}{B}]
{B}╚══[{R}OPTION{B}]═> {C}~ {Y}$ {RE}""")
        if x == '1':
            showInfo()
        elif x == '2':
            break
        elif x == '3':
            spammer()
            break
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
            gui()

def showInfo():
    print("Loading information...")
    os.system("neofetch")

def spammer():
    now = datetime.datetime.now()
    while True:
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
        while not rate.isdigit():
            print("\033[F\033[K", end="")
            print(f"{R}Invalid rate!")
            time.sleep(1.5)
            print("\033[F\033[K", end="")
            rate = input(f"{C}> {w}Enter rate (in seconds): ")
        rate = float(rate)

        cooldown = input(f"{C}> {w}Enter cooldown (in seconds): ")
        while not cooldown.isdigit():
            print("\033[F\033[K", end="")
            print(f"{R}Invalid cooldown!")
            time.sleep(1.5)
            print("\033[F\033[K", end="")
            cooldown = input(f"{C}> {w}Enter cooldown (in seconds): ")
        cooldown = float(cooldown)
        break

    tries = 0
    counter = 0
    current_time = now.strftime("%H:%M:%S")
    response = requests.post(url, json={"content": msg})
    print("\033[F"*4, "\033[K", "\033[K", "\033[K", "\033[K", "\033[K")
    print("\n")
    print(f"\n{C}> {w}Press 'Q' to stop.")
    print(f"{C}{current_time} {w}=> {R}[{response.status_code}] {w}Attempting to send {Y}'{msg}' {w}to '{url}' every {R}{rate} {w}seconds")
    while True:
        if msvcrt.kbhit() and msvcrt.getch() == b"q":
            print(f"{R}Exiting...{RE}")
            return
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

if __name__ == "__main__":
    start()
