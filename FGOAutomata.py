from colorama import Fore
from configparser import ConfigParser
import random
import time
from pynput.mouse import Button, Controller
import calibration 

config = ConfigParser()
config.read("config.ini")
mouse = Controller()

def Squick():
    return Fore.GREEN + "Quick" + Fore.WHITE

def Sbuster():
    return Fore.RED + "Buster" + Fore.WHITE
    
def Sarts():
    return Fore.BLUE + "Arts" + Fore.WHITE
    
def servant_skill(servant, skill):
    values = [int(num) for num in config["Servant {0}".format(servant)]["skill_{0}".format(skill)].split()]
    x = random.randint(values[0]+5, values[2]-5)
    y = random.randint(values[1]+5, values[3]-5)
    print("x: {0}".format(x) + "\ty: {0}".format(random.randint(values[1], values[3])))
    mouse.position = (x, y)
    mouse.move(1, 0)
    mouse.move(-1, 0)
    mouse.press(Button.left)
    mouse.release(Button.left)


time.sleep(1)
for i in range(1,4,1):
    for j in range(1,4,1):
            print("i: {0}\tj: {1}".format(i,j))
            servant_skill(i, j)
            time.sleep(1)

