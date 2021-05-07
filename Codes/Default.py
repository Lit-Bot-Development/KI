import sys
import os
import json
import datetime
from datetime import datetime
from os import system
import sysconfig
import time

with open(f"C:/Users/{os.getlogin()}/Documents/GitHub/KI/Codes/Codes.json") as f:
    data = json.load(f)

def cls():
    cls = lambda: system('cls')
    cls()

def startup():
    print(data)

cls()