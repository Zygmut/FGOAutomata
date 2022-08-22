from pynput.mouse import Listener, Controller 
from configparser import ConfigParser

config = ConfigParser()

def on_click(x, y, button, pressed):
    if not pressed:
        return False
    
def mouse_click_coords():
    with Listener(
        on_click=on_click
    ) as listener:
        mouse = Controller()
        listener.join()

    return mouse.position

''' 
This procedure should get the position all the necessary buttons a basic mission should have and save them in a dictionary type file. Those include, but are not limited to:
 · Servant skills
 · Each attack card and NP
 · Attack button
 · Mystic Code
'''
def calibration():

    print("Calibration procedure")
    config.read("config.ini")

    # Servants
    #cali_servants()

    # NP cards
    # cali_NP_cards()

    # Attack button 
    #cali_attack_butt()

    # Face cards 
    cali_face_cards()

    # Mystic code 
    #cali_mystic_code()

    # Enemy Servants
    #cali_enemy_servants() 

    # Servant skill target 

    # Mystic code Exchange display
    # cali_exchange_MC()
    

    # Save file
    with open('config.ini', 'w') as configFile:
        config.write(configFile)


# Method to calibrate all servant skills 
def cali_servants():
    for i in range(1,4,1): 
        print("\nCalibrating Servant {}".format(i))
        config["Servant {}".format(i)] = {}
        for j in range(1,4,1): # All skills
            coords = get_box_coords()
            print("Skill_{0} at {1}".format(j,coords))
            config["Servant {}".format(i)]["skill_{}".format(j)] = ' '.join(str(e) for e in [coords[0], coords[1], coords[2], coords[3]])


# Method to calibrate attack button placement
def cali_attack_butt():
    print("\nCalibrating Attack button")
    config["Attack button"] = {}
    coords = get_box_coords()
    print("Attack button at {}".format(coords))
    config["Attack button"]["coords"] = ' '.join(str(e) for e in [coords[0], coords[1], coords[2], coords[3]])


# Method to calibrate mystic code button and skills
def cali_mystic_code():
    print("\nCalibrating Mystic code")
    config["Mystic code"] = {}
    coords = get_box_coords()
    print("Mystic code at {}".format(coords))
    config["Mystic code"]["coords"] = ' '.join(str(e) for e in [coords[0], coords[1], coords[2], coords[3]])
    mouse_click_coords() # we need to click the mystic code again. This is a dummy click
    for j in range(1,4,1): # All skills
            coords = get_box_coords()
            print("Skill_{0} at {1}".format(j,coords))
            config["Mystic code"]["skill_{}".format(j)] = ' '.join(str(e) for e in [coords[0], coords[1], coords[2], coords[3]])

# Method to calibrate exchange mystic code skill
def cali_exchange_MC():
    print("\nCalibrating Mystic code exchange")
    config["Exchange Mystic code"] = {}

    coords = get_box_coords()
    print("Accept button at: {0}".format(coords))
    config["Exchange Mystic code"]["accept"] = ' '.join(str(e) for e in [coords[0], coords[1], coords[2], coords[3]])

    for j in range(1,7,1): # All skills
            coords = get_box_coords()
            print("Card_{0} at {1}".format(j,coords))
            config["Exchange Mystic code"]["card_{}".format(j)] = ' '.join(str(e) for e in [coords[0], coords[1], coords[2], coords[3]])


# Method to calibrate all face cards 
def cali_face_cards():
    print("\nCalibrating Face cards")
    config["Face cards"] = {}
    for j in range(1,6,1): # All skills
            coords = get_box_coords()
            print("Card_{0} at {1}".format(j,coords))
            config["Face cards"]["card_{}".format(j)] = ' '.join(str(e) for e in [coords[0], coords[1], coords[2], coords[3]])
    
# Method to calibrate all NP cards
def cali_NP_cards():
    print("\nCalibrating NP cards")
    config["NP cards"] = {}
    for j in range(1,4,1): # All skills
            coords = get_box_coords()
            print("Card_{0} at {1}".format(j,coords))
            config["NP cards"]["card_{}".format(j)] = ' '.join(str(e) for e in [coords[0], coords[1], coords[2], coords[3]])

#Method to get the coords of to given points making a box, returns x1, y1, x2, y2
def get_box_coords():
    f1_click = mouse_click_coords()
    s1_click = mouse_click_coords()
    return [f1_click[0], f1_click[1], s1_click[0], s1_click[1]]


def mouse_coordinate():
    click1 = mouse_click_coords()
    click2 = mouse_click_coords()
    print("x1:{0} y1:{1}\tx2:{2} y2:{3}".format(
        click1[0], click1[1], click2[0], click2[1]
    ))

calibration()