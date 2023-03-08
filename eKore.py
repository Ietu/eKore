import time
import datetime
import os
import subprocess
import curses
import shutil
import requests
import threading
import json
import msvcrt
import discord
import sys
import tools.discord
from rich.progress import Progress
from rich import align
from lolpython import lol_py 
from tqdm import tqdm
from colorama import Fore, init, Style
from tools import discord

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

def start():
    os.system('cls')
    curses.wrapper(scrollText)
    gui()
    menu()

def scrollText(stdscr):
    message = f"Logging in as {username}@"
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
                                 {B}╔═══════════════════╦═══════════════════╗{w}
                                 {B}║ {w}[{C}1{w}] Quit          {B}║ {w}[{C}2{w}] Show Sys Info {B}║{w}
                                 {B}║ {w}[{C}3{w}] Discord Tools {B}║ {w}[{C}4{w}] File Tools    {B}║{w}
                                 {B}║ {w}[{C}5{w}] Text Editor   {B}║ {w}[{C}6{w}] Network Tools {B}║{w}
                                 {B}║ {w}[{C}7{w}] Image Tools   {B}║ {w}[{C}8{w}] -             {B}║{w}
                                 {B}║ {w}[{C}9{w}] Game Launcher {B}║ {w}[{C}10{w}] -            {B}║{w}
                                 {B}║ {w}[{C}11{w}] -            {B}║ {w}[{C}12{w}] -            {B}║{w}
                                 {B}║ {w}[{C}13{w}] -            {B}║ {w}[{C}14{w}] -            {B}║{w}
                                 {B}╚═══════════════════╩═══════════════════╝{w} 
""")      
    
def menu():
    os.system("cls")
    gui()
    while True:
        x = input(f"""
{B}╔═{B}[{C}{pcname}{Y}@{C}{username}{B}]
{B}╚══[{R}OPTION{B}]═> {C}~ {Y}$ {RE}""")
        if x == '1':
            exit()
        elif x == '2':
            showInfo()
        elif x == '3':
            tools.discord.start()
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
    with Progress() as progress:
        task1 = progress.add_task("[white]Loading information...", total=1000)
        task2 = progress.add_task("[white]Processing...", total=1000)
        while not progress.finished:
            progress.update(task1, advance=15)
            progress.update(task2, advance=10)
            time.sleep(0.02)
    
    os.system("neofetch -c BLUE -ac BLUE")
    print(f"Press '{R}Enter{w}' to go back.")



if __name__ == "__main__":
    start()