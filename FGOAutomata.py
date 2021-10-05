from colorama import Fore
from configparser import ConfigParser
import random
import time
from pynput.mouse import Button, Controller
import calibration 

SKILL_MARGIN = 3

config = ConfigParser()
config.read("config.ini")
mouse = Controller()

def Squick():
    return Fore.GREEN + "Quick" + Fore.WHITE

def Sbuster():
    return Fore.RED + "Buster" + Fore.WHITE
    
def Sarts():
    return Fore.BLUE + "Arts" + Fore.WHITE
    
def disp_click(x, y):
    mouse.position = (x, y)
    #We need to move the mouse to update actal position 
    mouse.move(1, 0)
    mouse.move(-1, 0)
    mouse.press(Button.left)
    mouse.release(Button.left)


# Use servant skill with no targets (ex: carisma EX, Mana burst A)
def servant_skill(servant, skill):
    # Read servantvalues from config 
    values = [int(num) for num in config["Servant {0}".format(servant)]["skill_{0}".format(skill)].split()]

    # Create random coordinates inside coords box 
    x = random.randint(values[0]+SKILL_MARGIN, values[2]-SKILL_MARGIN)
    y = random.randint(values[1]+SKILL_MARGIN, values[3]-SKILL_MARGIN)

    print("\nServant {0} -> skill_{1}".format(servant, skill))
    print("x: {0}".format(x) + "\ty: {0}".format(y))

    disp_click(x,y)


# Use servant skill with target (ex: Hero creation EX) 
# Even tho one can make this command by hand, we think it's handy to have it
def servant_skill_target(servant, skill, target):
    # Read servantvalues from config 
    servant_skill(servant, skill)
    
    # target servant 
    target_servant(target)

# Should set target to mystic code and servant skills.
def target_servant(target):

    return True


time.sleep(1)
for i in range(1,4,1):
    for j in range(1,4,1):
            for h in range(1,4,1):
                
                servant_skill(i, j)
                time.sleep(2)

