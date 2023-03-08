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
from tools.utiltools import colorpicker
from rich.progress import Progress
from rich import align
from lolpython import lol_py 
from tqdm import tqdm
from colorama import Fore, init, Style


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

def utilGui():
    os.system("cls")
    print(f"""
               {B}────────────────────────────────────────────────────────────────────────────{w}
               {C}██╗   ██╗████████╗██╗██╗         ████████╗ ██████╗  ██████╗ ██╗     ███████╗
               {C}██║   ██║╚══██╔══╝██║██║         ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
               {C}██║   ██║   ██║   ██║██║            ██║   ██║   ██║██║   ██║██║     ███████╗
               {C}██║   ██║   ██║   ██║██║            ██║   ██║   ██║██║   ██║██║     ╚════██║
               {C}╚██████╔╝   ██║   ██║███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
               {C} ╚═════╝    ╚═╝   ╚═╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
               {B}────────────────────────────────────────────────────────────────────────────{w}
                                 {B}╔═══════════════════╦═══════════════════╗{w}
                                 {B}║ {w}[{C}1{w}] Main Menu     {B}║ {w}[{C}2{w}] Quit          {B}║{w}
                                 {B}╠═══════════════════╬═══════════════════╣
                                 {B}║ {w}[{C}3{w}] Colorpicker   {B}║ {w}[{C}4{w}] -             {B}║{w}
                                 {B}║ {w}[{C}5{w}] -             {B}║ {w}[{C}6{w}] -             {B}║{w}
                                 {B}║ {w}[{C}7{w}] -             {B}║ {w}[{C}8{w}] -             {B}║{w}
                                 {B}║ {w}[{C}9{w}] -             {B}║ {w}[{C}10{w}] -            {B}║{w}
                                 {B}║ {w}[{C}11{w}] -            {B}║ {w}[{C}12{w}] -            {B}║{w}
                                 {B}║ {w}[{C}13{w}] -            {B}║ {w}[{C}14{w}] -            {B}║{w}
                                 {B}╚═══════════════════╩═══════════════════╝{w} 
""")      

def start():
    utilGui()
    menu()

def menu():
    while True:
        x = input(f"""
{B}╔═{B}[{C}{pcname}{Y}@{C}{username}{B}]
{B}╚══[{R}OPTION{B}]═> {C}~ {Y}$ {RE}""")
        if x == '1':
            eKore.menu()
        elif x == '2':
            print(f"{R}Quitting...{RE}")
            time.sleep(1)
            os.system("cls")
            exit()
        elif x == '3':
            colorpicker.start()
            os.system("cls")
            start()
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
            utilGui()