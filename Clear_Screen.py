from OSDetect import osDetect
import os

def clear_Screen():
    syst = osDetect()

    if syst=='W':
        clear = lambda: os.system('cls') #on Windows System
        clear()

    elif syst=='M':
        clear = lambda: os.system('clear') #on Linux System
        clear() 

    elif syst=='L':
        clear = lambda: os.system('clear') #on Linux System
        clear()