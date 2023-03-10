import os
import pyfiglet
import curses
import time
from pyfiglet import Figlet

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

def showcase(text):
    font_list = pyfiglet.FigletFont.getFonts()
    max_width = os.get_terminal_size().columns

    for font in font_list:
        figlet = Figlet(font=font)
        rendered_width = len(figlet.renderText(text))
        if rendered_width > max_width:
            figlet.width = max_width
        print(f"\n{font}")
        print(figlet.renderText(text))
    print(f"{C}> {w}Previews printed.")

def start():
    preview = input(f"{C}> {w}Do you want to see all fonts previewed?(Y/N): ")
    text = input(f"{C}> {w}Enter text: ")
    if preview.capitalize() == 'Y':
        showcase(text)
    else:
        while True:
            font = input(f"{C}> {w}Enter font name (press Enter for default): ") or "univers"
            try:
                figlet = pyfiglet.Figlet(font=font)
                break
            except:
                print(f"{C}> {R}Invalid font name!{w}")
                time.sleep(2)
                print("\033[F\033[K", end="")
                print("\033[F\033[K", end="")
    print(f"{C}> {w}Press '{R}Enter{RE}' to exit.")

if __name__ == "__main__":
    start()