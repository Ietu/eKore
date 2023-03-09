import pyautogui
import time
import webcolors
import keyboard

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

def get_color():
    x, y = pyautogui.position()
    color = pyautogui.screenshot().getpixel((x, y))
    hex_color = webcolors.rgb_to_hex(color)
    return hex_color, color

def start():
    print(f"{C}> {w}Press '{R}V{w}' to get the color values under the cursor.")
    print(f"{C}> {w}Press '{R}Q{w}' to exit.")
    while True:
        if keyboard.is_pressed('V'):
            hex_color, color = get_color()
            print(f"HEX: {hex_color}")
            print(f"RGB: {color}\n")
            time.sleep(1)
        if keyboard.is_pressed('Q'):
            print(f"{R}Exiting...{RE}")
            time.sleep(1)
            break

if __name__ == "__main__":
    start()