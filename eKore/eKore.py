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
from tools import settings
from tools.utiltools import utilmenu
from tools.discordtools import discord
from tools.filetools import filetool
from tools.networktools import networkmenu
from rich.progress import Progress
from rich import align
from lolpython import lol_py 
from tqdm import tqdm
from colorama import Fore, init, Style


os.system("cls")

# pcname = "PCNAME"
# username = "USERNAME"

center = shutil.get_terminal_size().columns
height, width = shutil.get_terminal_size()
pcname = (os.getenv('COMPUTERNAME'))
username = os.getlogin()

# Determine the number of blank lines to print before and after the text
num_lines_before = int((height - 1) / 2)  # subtract 7 for the number of lines in the text
num_lines_after = height - num_lines_before - 1

#pcname = "PCNAME"
#username = "USERNAME"

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
    time.sleep(1.5)

def gui():
    os.system("cls")
    print(f"""
                                 {C}─────────────────────────────────────────{w}
                                 {R}███████╗██╗  ██╗ ██████╗ ██████╗ ███████╗
                                 {R}██╔════╝██║ ██╔╝██╔═══██╗██╔══██╗██╔════╝
                                 {R}█████╗  █████╔╝ ██║   ██║██████╔╝█████╗  
                                 {R}██╔══╝  ██╔═██╗ ██║   ██║██╔══██╗██╔══╝  
                                 {R}███████╗██║  ██╗╚██████╔╝██║  ██║███████╗
                                 {R}╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝            
                                 {C}─────────────────────────────────────────{w}
                                 {C}╔═══════════════════╦═══════════════════╗{w}
                                 {C}║ {w}[{R}1{w}] Quit          {C}║ {w}[{R}2{w}] Settings      {C}║{w}
                                 {C}╠═══════════════════╬═══════════════════╣
                                 {C}║ {w}[{R}3{w}] Discord Tools {C}║ {w}[{R}4{w}] File Tools    {C}║{w}
                                 {C}║ {w}[{R}5{w}] Text Editor   {C}║ {w}[{R}6{w}] Network Tools {C}║{w}
                                 {C}║ {w}[{R}7{w}] Image Tools   {C}║ {w}[{R}8{w}] Util Tools    {C}║{w}
                                 {C}║ {w}[{R}9{w}] Games         {C}║ {w}[{R}10{w}] Show Sys Info{C}║{w}
                                 {C}║ {w}[{R}11{w}] -            {C}║ {w}[{R}12{w}] -            {C}║{w}
                                 {C}║ {w}[{R}13{w}] -            {C}║ {w}[{R}14{w}] -            {C}║{w}
                                 {C}╚═══════════════════╩═══════════════════╝{w} 
""".center(center))
    
def validCommand(command):
    if command.isdigit() and (int(command) < 1 or int(command) > 14):
        menu()
    elif (command, str) and len(command) > 0:
        subprocess.Popen(f"powershell {command}")
        print(f"{C}> {w}Press '{R}Enter{w}' to go back.")
        input()
    else:
        return


def menu():
    defaultDir = "~"
    os.system("cls")
    gui()
    while True:
        x = input(f"""
{C}╔═{C}({R}{pcname}{Y}㉿{R}{username}{C})-[{w}{defaultDir}{C}]
{C}╚══[{B}OPTION{C}]═> {Y}$ {RE}""")
        if x == '1':
            print(f"{R}Quitting...{RE}")
            time.sleep(1)
            os.system("cls")
            print("\n" * 7)
            print(f"""
                      {C} ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗██╗
                      {C}██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝██║
                      {C}██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗  ██║
                      {C}██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝
                      {C}╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗██╗
                      {C} ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝
            """)
            time.sleep(2)
            os.system("cls")
            exit()
        elif x == '2':
            settings.start()
        elif x == '3':
            discord.start()
        elif x == '4':
            filetool.start()
        elif x == '5':
            print(f"{R}Exiting...")
            time.sleep(1)
            exit()
        elif x == '6':
            networkmenu.start()
        elif x == '7':
            print(f"{R}Exiting...")
            time.sleep(1)
            exit()
        elif x == '8':
            utilmenu.start()
        elif x == '9':
            print(f"{R}Exiting...")
            time.sleep(1)
            exit()
        elif x == '10':
            showInfo()
        elif x == '11':
            print(f"{R}Exiting...")
            time.sleep(1)
            exit()
        elif x == '12':
            print(f"{R}Exiting...")
            time.sleep(1)
            exit()
        elif x == '13':
            print(f"{R}Exiting...")
            time.sleep(1)
            exit()
        elif x == '14':
            print(f"{R}Exiting...")
            time.sleep(1)
            exit()
        elif x == validCommand(x):
            os.system("cls")
            gui()
        else:
            #print(f"{R}Invalid option! Please select a valid option.")
            #time.sleep(1)
            os.system("cls")
            gui()

def showInfo():
    with Progress() as progress:
        task1 = progress.add_task(f"{C}> {w}[white]Loading information...", total=1000)
        task2 = progress.add_task(f"{C}> {w}[white]Processing...", total=1000)
        while not progress.finished:
            progress.update(task1, advance=15)
            progress.update(task2, advance=10)
            time.sleep(0.02)
    print("\033[K\033[K")
    os.system("neofetch -c BLUE -ac BLUE")
    print(f"{C}> {w}Press '{R}Enter{w}' to go back.")

if __name__ == "__main__":
    start()