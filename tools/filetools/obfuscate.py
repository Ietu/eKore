import binascii
import bz2
import gzip
import lzma
import marshal
import random
import time
import zlib
import msvcrt
import os
from rich.progress import Progress
from tkinter import Tk, filedialog

P = "\033[35m" # pink
G1 = "\033[90m" # grey
w = "\033[37m" # white
P = "\033[35m" # purple
R = "\033[31m" # red
G = "\033[32m" # green
C = "\033[36m" # cyan
RE = "\033[0m" # reset
Y = "\033[33m" # yellow
B = "\033[34m" # blue
LG = "\033[37m" # lightgrey


def encode(source: str) -> str:
    selected_mode = random.choice((lzma, gzip, bz2, binascii, zlib))
    marshal_encoded = marshal.dumps(compile(source, "Scorch", "exec"))
    if selected_mode is binascii:
        encoded = binascii.b2a_base64(marshal_encoded)
    else:
        encoded = selected_mode.compress(marshal_encoded)
    if selected_mode is binascii:
        TMP = "import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(binascii.a2b_base64({})))"
        return TMP.format(encoded)
    else:
        TMP = "import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads({}.decompress({})))"
        return TMP.format(selected_mode.__name__, encoded)

def getArgs():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    output_name = input(f"{C}> {w}Enter the output file name: ")
    strength = 100
    return file_path, output_name, strength


def start():
    file_path, output_name, strength = getArgs()
    print(f"{C}> {w}Encoding " + file_path)
    with open(file_path, "r") as f:
        source = f.read()
        with Progress() as progress:
            task1 = progress.add_task(f"{C}> {w}[white]Encoding...", total=strength)
            encoded = source
            for i in range(strength):
                encoded = encode(source=encoded)
                time.sleep(0.1)
                progress.update(task1, advance=1)

    with open(output_name, "w") as f:
        f.write(encoded)

    print(f"{C}> {w}Encoding successful!\n{C}> {w}Saved as '{C}{output_name}{RE}'")
    print(f"\n{C}> {w}Press '{R}Enter{RE}' to exit.")
    input()

if __name__ == "__main__":
    start()