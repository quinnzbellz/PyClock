import datetime
import time
from os import system, name

def clr():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


while True:
    tme = datetime.datetime.now()
    print(tme.strftime("%H:%M"))
    time.sleep(1)
    clr()