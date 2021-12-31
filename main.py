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

def print_centre(s):
    tprint(s.center(shutil.get_terminal_size().columns))

clr()
time.sleep(0.4)
# Starts an infinite loop of showing the time
while True:
    tme = datetime.datetime.now()
    b = str(tme.strftime("%H:%M"))
    print_centre(b)
    time.sleep(1)
    clr()