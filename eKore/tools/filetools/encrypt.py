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

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(file_path + ".encrypted", 'wb') as f:
        f.write(encrypted)
    os.remove(file_path)

def encrypt_folder(folder_path):
    key = Fernet.generate_key()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'output'))
    output_path = os.path.join(file_path, 'key.txt')
    with open(output_path, 'wb') as key_file:
        key_file.write(key)
        print(f"{C}> {w}Enryption key: {key}")
        print(f"{C}> {w}Encryption key location: {file_path}")
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)


def start():
    folder_path = filedialog.askdirectory()
    confirm = input(f"{C}> {w}Do you really want to ENCRYPT all files in the folder?(Y/N): ")
    if confirm.capitalize() == "Y":
        encrypt_folder(folder_path)
        print(f"{R}Files Encrypted.")
        print(f"Press '{R}Enter{RE}' to exit.")
        input()
    else:
        print(f"{R}Cancelled")
        time.sleep(2)

if __name__ == '__main__':
    start()