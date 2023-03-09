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
from tools.filetools import obfuscate, encrypt, decrypt
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

def fileGui():
    os.system("cls")
    print(f"""
               {C}────────────────────────────────────────────────────────────────────────────{w}
                {R}███████╗██╗██╗     ███████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                {R}██╔════╝██║██║     ██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                {R}█████╗  ██║██║     █████╗         ██║   ██║   ██║██║   ██║██║     ███████╗
                {R}██╔══╝  ██║██║     ██╔══╝         ██║   ██║   ██║██║   ██║██║     ╚════██║
                {R}██║     ██║███████╗███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                {R}╚═╝     ╚═╝╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
               {C}────────────────────────────────────────────────────────────────────────────{w}
                                 {C}╔═══════════════════╦═══════════════════╗{w}
                                 {C}║ {w}[{R}1{w}] Main Menu     {C}║ {w}[{R}2{w}] Quit          {C}║{w}
                                 {C}╠═══════════════════╬═══════════════════╣
                                 {C}║ {w}[{R}3{w}] Obfuscate Py  {C}║ {w}[{R}4{w}] -             {C}║{w}
                                 {C}║ {w}[{R}5{w}] -             {C}║ {w}[{R}6{w}] -             {C}║{w}
                                 {C}║ {w}[{R}7{w}] -             {C}║ {w}[{R}8{w}] -             {C}║{w}
                                 {C}║ {w}[{R}9{w}] -             {C}║ {w}[{R}10{w}] -            {C}║{w}
                                 {C}║ {w}[{R}11{w}] -            {C}║ {w}[{R}12{w}] -            {C}║{w}
                                 {C}║ {w}[{R}13{w}] Encrypt Files{C}║ {w}[{R}14{w}] Decrypt Files{C}║{w}
                                 {C}╚═══════════════════╩═══════════════════╝{w} 
""")      

def start():
    fileGui()
    menu()

def menu():
    defaultDir = "~/File"
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
            obfuscate.start()
            os.system("cls")
            start()
        elif x == '4':
            break
        elif x == '5':
            break
        elif x == '6':
            break
        elif x == '7':
            break
        elif x == '8':
            break
        elif x == '9':
            break
        elif x == '10':
            break
        elif x == '11':
            break
        elif x == '12':
            break
        elif x == '13':
            encrypt.start()
            os.system("cls")
            start()
        elif x == '14':
            decrypt.start()
            os.system("cls")
            start()
        else:
            print(f"{R}Invalid option! Please select a valid option.")
            time.sleep(1)
            os.system("cls")
            fileGui()