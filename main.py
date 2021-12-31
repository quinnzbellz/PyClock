# Import libraries
import datetime
import time
import termios
import struct
import fcntl
from os import system, name
from art import tprint

# Define a clear command to make clock update
def clr():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

cols = system('tput cols')
clr()
time.sleep(0.4)
# Starts an infinite loop of showing the time
while True:
    num2 = 2
    width = 18
    c = int(cols / num2 - width * 3)
    tme = datetime.datetime.now()
    b = str(tme.strftime("%H:%M"))
    a = b.center(c)
    tprint(a)
    time.sleep(1)
    clr()