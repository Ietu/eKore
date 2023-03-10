import os
import tkinter as tk
import eKore
import time
from tkinter import filedialog
from cryptography.fernet import Fernet

pcname = (os.getenv('COMPUTERNAME'))
username = os.getlogin()

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

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    with open(os.path.splitext(file_path)[0], 'wb') as f:
        f.write(decrypted)
    os.remove(file_path)

def decrypt_folder(folder_path):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'output'))
    output_path = os.path.join(file_path, 'key.txt')
    try:
        with open(output_path, 'rb') as key_file:
            key = key_file.read()
            print(f"{C}> {w}Deryption key: {key}")
            print(f"{C}> {w}Decryption key location: {file_path}")
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.endswith(".encrypted"):
                    decrypt_file(file_path, key)
    except:
        print(f"{C}> {R}Error: Decrypt key file not found!{w}")
        

def start():
    folder_path = filedialog.askdirectory()
    confirm = input(f"{C}> {w}Do you really want to DECRYPT all files in the folder?(Y/N): ")
    if confirm.capitalize() == "Y":
        decrypt_folder(folder_path)
        print(f"{R}Files Decrypted.")
        print(f"Press '{R}Enter{RE}' to exit.")
        input()
    else:
        print(f"{R}Cancelled")
        time.sleep(2)

if __name__ == '__main__':
    start()