from pynput.mouse import Listener, Controller 
from configparser import ConfigParser

CONFIG = ConfigParser()
CONFIG_FILE = "config2.ini"

#DEBUG 
DEBUG = True
def debug(s: str) -> None:
    if DEBUG: print(f"[DEBUG] {s}")

# Mouse listener 
def on_click(x, y, button, pressed) -> bool:
    if not pressed:
        return False
    
def get_mouse_coords() -> (int):
    with Listener(
        on_click=on_click
    ) as listener:
        mouse = Controller()
        listener.join()

    return mouse.position

# Misc 
def get_box_coords() -> (int):
    return (get_mouse_coords() + get_mouse_coords())

# Methods  
def servant_skills() -> None:
    for i in range(3):
        debug(f"Calibrating servant {i}")
        CONFIG[f"Servant {i}"] = {}

        for j in range(3):
            coords = get_box_coords()
            debug(f"Skill {j} at {coords}")
            CONFIG[f"Servant {i}"][f"skill_{j}"] = ' '.join(str(value) for value in coords)

def target_skill() -> None:
    debug("Calibrating target skills")    
    CONFIG["Target skills"] = {}
    for i in range(3):
        coords = get_box_coords()
        debug(f"Servant {i} at {coords}")
        CONFIG["Target skills"][f"servant_{i}"] = ' '.join(str(value) for value in coords)

def enemies() -> None:
    debug("Calibrating enemies")    
    CONFIG["Enemies"] = {}
    for i in range(3):
        coords = get_box_coords()
        debug(f"Enemy {i} at {coords}")
        CONFIG["Enemies"][f"coord_{i}"] = ' '.join(str(value) for value in coords)

def attack_button() -> None:
    debug("Calibrating attack button")
    CONFIG["Attack button"] = {}
    coords = get_box_coords()
    debug(f"Attack button at {coords}")
    CONFIG["Attack button"]["coords"] = ' '.join(str(value) for value in coords)
    
def mystic_code() -> None:
    debug("Calibrating mystic code ")    
    CONFIG["Mystic code"] = {}
    coords = get_box_coords()
    debug(f"Mystic code coords at {coords}")
    CONFIG["Mystic code"]["coords"] = ' '.join(str(value) for value in coords)
    debug("Calibrating mystic code skills") 
    for i in range(3):
        coords = get_box_coords()
        debug(f"MC skill {i} at {coords}")
        CONFIG["Mystic code"][f"skill_{i}"] = ' '.join(str(value) for value in coords)

def mystic_code_exchange() -> None:
    debug("Calibrating Mystic code exchange")    
    CONFIG["Exchange"] = {}
    for i in range(6):
        coords = get_box_coords()
        debug(f"Servant {i} at {coords}")
        CONFIG["Exchange"][f"servant_{i}"] = ' '.join(str(value) for value in coords)

def servant_face_cards() -> None:
    debug("Calibrating Face cards")    
    CONFIG["Face cards"] = {}
    for i in range(5):
        coords = get_box_coords()
        debug(f"Card {i} at {coords}")
        CONFIG["Face cards"][f"card_{i}"] = ' '.join(str(value) for value in coords)
     
def servant_NP() -> None:
    debug("Calibrating NP cards")    
    CONFIG["NP cards"] = {}
    for i in range(3):
        coords = get_box_coords()
        debug(f"Card {i} at {coords}")
        CONFIG["NP cards"][f"card_{i}"] = ' '.join(str(value) for value in coords)
            
def calibrate(config_file = CONFIG_FILE):
    calibrating2 = (servant_NP, servant_face_cards, servant_skills, mystic_code, mystic_code_exchange, attack_button, enemies, target_skill)
    calibrating = (mystic_code, attack_button)
    print("Calibration procedure")    
    CONFIG.read(config_file)
    for procedure in calibrating:
        input(f"Next up is {procedure.__name__}, press ENTER to proceed ...") 
        procedure()

    with open(config_file, "w") as file:
        CONFIG.write(file)

if __name__ == "__main__":
    calibrate()