import time
import os
import shutil
import eKore
from tools.games import coin
from rich.progress import Progress

center = shutil.get_terminal_size().columns
pcname = (os.getenv('COMPUTERNAME'))
username = os.getlogin()

# pcname = "PCNAME"
# username = "USERNAME"


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

def gameGui():
    os.system("cls")
    print(f"""
                                {C}──────────────────────────────────────────{w}
                               {R} ██████╗  █████╗ ███╗   ███╗███████╗███████╗
                               {R}██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝
                               {R}██║  ███╗███████║██╔████╔██║█████╗  ███████╗
                               {R}██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║
                               {R}╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║
                               {R} ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝
                                {C}──────────────────────────────────────────{w}
                                 {C}╔═══════════════════╦═══════════════════╗{w}
                                 {C}║ {w}[{R}1{w}] Main Menu     {C}║ {w}[{R}2{w}] Quit          {C}║{w}
                                 {C}╠═══════════════════╬═══════════════════╣
                                 {C}║ {w}[{R}3{w}] Coin flipper  {C}║ {w}[{R}4{w}] -             {C}║{w}
                                 {C}║ {w}[{R}5{w}] -             {C}║ {w}[{R}6{w}] -             {C}║{w}
                                 {C}║ {w}[{R}7{w}] -             {C}║ {w}[{R}8{w}] -             {C}║{w}
                                 {C}║ {w}[{R}9{w}] -             {C}║ {w}[{R}10{w}] -            {C}║{w}
                                 {C}║ {w}[{R}11{w}] -            {C}║ {w}[{R}12{w}] -            {C}║{w}
                                 {C}║ {w}[{R}13{w}] -            {C}║ {w}[{R}14{w}] -            {C}║{w}
                                 {C}╚═══════════════════╩═══════════════════╝{w} 
""")      

def start():
    gameGui()
    menu()

def menu():
    defaultDir = "~/Games"
    while True:
        x = input(f"""
{C}╔═{C}({R}{pcname}{Y}㉿{R}{username}{C})-[{w}{defaultDir}{C}]
{C}╚══[{B}OPTION{C}]═> {Y}$ {RE}""")
        if x == '1':
            eKore.menu()
        elif x == '2':
            print(f"{R}Quitting...{RE}")
            time.sleep(1)
            os.system("cls")
            exit()
        elif x == '3':
            coin.main()
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
            gameGui()