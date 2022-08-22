from colorama import Fore
from configparser import ConfigParser
import random
import time
from pynput.mouse import Button, Controller
from calibrationV2 import calibrate 

SKILL_MARGIN = 10
SPEED = 1

config = ConfigParser()
config.read("config.ini")
mouse = Controller()

def Squick():
    return Fore.GREEN + "Quick" + Fore.WHITE

def Sbuster():
    return Fore.RED + "Buster" + Fore.WHITE
    
def Sarts():
    return Fore.BLUE + "Arts" + Fore.WHITE
    
# Method that click on the display at (x,y)
def disp_click(x, y):
    mouse.position = (x, y)
    #We need to move the mouse to update actal position 
    mouse.move(1, 0)
    mouse.move(-1, 0)
    mouse.press(Button.left)
    mouse.release(Button.left)

# Method to apply a random function uppon 4 coordinates values passed
# as an argument. It also aplies a certain margin
def get_ran_click_coords(values):
    x = random.randint(values[0]+SKILL_MARGIN, values[2]-SKILL_MARGIN)
    y = random.randint(values[1]+SKILL_MARGIN, values[3]-SKILL_MARGIN)
    print("x: {0}".format(x), "\ty: {0}".format(y))
    return (x,y)

def ran_disp_click(values):
    coords = get_ran_click_coords(values)
    
    disp_click(coords[0], coords[1])

# Use servant skill with no targets (ex: carisma EX, Mana burst A)
def servant_skill(servant, skill):
    # Read servantvalues from config 
    values = [int(num) for num in config["Servant {0}".format(servant)]["skill_{0}".format(skill)].split()]

    # Create random coordinates inside coords box 
    print("\nServant {0} -> skill_{1}".format(servant, skill))
    ran_disp_click(values)


# Use exchange Mystic code skill
def exchange_servants(outgoing, ingoing):
    mystic_code_skill(3)

    time.sleep(SPEED)

    values = [int(num) for num in config["Exchange Mystic code"]["card_{}".format(outgoing)].split()]
    ran_disp_click(values)
    
    time.sleep(SPEED)

    values = [int(num) for num in config["Exchange Mystic code"]["card_{}".format(ingoing)].split()]
    ran_disp_click(values)

    time.sleep(SPEED)

    values = [int(num) for num in config["Exchange Mystic code"]["accept"].split()]
    ran_disp_click(values)


# Use Mystic code skill
def mystic_code_skill(skill):
    print("\nMystic code -> skill_{0}".format(skill))
    # Click mystic code button
    values_butt = [int(num) for num in config["Mystic code"]["coords"].split()]
    ran_disp_click(values_butt) # maybe can be disp_click(coords)

    time.sleep(SPEED)

    # Click mystic code skill
    values_skill = [int(num) for num in config["Mystic code"]["skill_{0}".format(skill)].split()]
    ran_disp_click(values_skill)
    
    
    
# Method to attack
def attack(commands):
    # Click Attack button
    values = [int(num) for num in config["Attack button"]["coords"].split()]
    ran_disp_click(values)
    

    for i in range(0,3,1):
        time.sleep(SPEED)
        if commands[i].split()[0] == "NP": # NP cards
            values = [int(num) for num in config["NP cards"]["card_{0}".format(commands[i].split()[1])].split()]

        elif commands[i].split()[0] == "FC": # Face cards
            values = [int(num) for num in config["Face cards"]["card_{0}".format(commands[i].split()[1])].split()]
        else:
            print("Error")
            return False
        ran_disp_click(values)

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

calibrate("config_2.ini")
'''
time.sleep(1)
for i in range(1,4,1):
    for j in range(1,4,1):
            for h in range(1,4,1):
                
                servant_skill(i, j)
                time.sleep(2)
'''





