# Import libraries
import datetime
import time
from os import system, name
from art import tprint

# Define a clear command to make clock update
def clr():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Starts an infinite loop of showing the time
while True:
    tme = datetime.datetime.now()
    b = str(tme.strftime("%H:%M"))
    tprint(b)
    time.sleep(1)
    clr()