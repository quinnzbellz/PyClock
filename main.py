# Import libraries
import datetime
import time
import shutil
from os import system, name
from art import tprint

# Define a clear command to make clock update
def clr():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')



clr()
time.sleep(0.4)
# Starts an infinite loop of showing the time
while True:
    tme = datetime.datetime.now()
    b = str(tme.strftime("%H:%M"))
    tprint(b)
    print(tme.strftime("%A %B %d %Y"))
    time.sleep(1)
    clr()