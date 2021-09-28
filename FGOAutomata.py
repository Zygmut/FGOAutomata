from colorama import Fore
from pynput.mouse import Listener, Controller 
from configparser import ConfigParser

def Squick():
    return Fore.GREEN + "Quick" + Fore.WHITE

def Sbuster():
    return Fore.RED + "Buster" + Fore.WHITE
    
def Sarts():
    return Fore.BLUE + "Arts" + Fore.WHITE

def on_click(x, y, button, pressed):
    if not pressed:
        return False
    

''' 
This procedure should get the position all the necessary buttons a basic mission should have and save them in a dictionary type file. Those include, but are not limited to:
 · Servant skills
 · Each attack card and NP
 · Attack button
 · Mystic Code
'''
def calibration():

    print("Calibration procedure")
    print("Click on the leftmost skill of your display")

    #Set delay, not clean but it works
    with Listener(
        on_click=on_click
    ) as listener:
        listener.join()

    f_click = mouse.position

    with Listener(
        on_click=on_click
    ) as listener:
        listener.join()

    s_click = mouse.position
    
    print("First skill is within {0} and {1} on the X axis and {2} and {3} on the y axis".format(
        f_click[0], s_click[0], f_click[1], s_click[1]
    ))
    

    # Once the first area is calibrated, generate all the other coordinates
    
    file_data = open("config.ini", 'r')
    config = ConfigParser()
    config.read(file_data)
    
    config['S1s1'] = {
        'x1' : f_click[0],
        'x2' : s_click[0],
        'y1' : f_click[1],
        'y2' : s_click[1],
    }

    # Save file
    file_data = open("config.ini", 'w')
    config.write(file_data)

    '''
    #create all servant skill sections
    config.add_section("S1s1")
    config.add_section("S1s2")
    config.add_section("S1s3")
    
    config.add_section("S2s1")
    config.add_section("S2s2")
    config.add_section("S2s3")
    
    config.add_section("S3s1")
    config.add_section("S3s2")
    config.add_section("S3s3")

    #Face cards
    config.add_section("fc1")
    config.add_section("fc2")
    config.add_section("fc3")
    config.add_section("fc4")
    config.add_section("fc5")

    #NP's
    config.add_section("np1")
    config.add_section("np2")
    config.add_section("np3")

    #Mystic code skills
    config.add_section("mc1")
    config.add_section("mc2")
    config.add_section("mc3")

    config.set("S1s1", "")
    '''
    


mouse = Controller()
print(mouse.position)
calibration()

