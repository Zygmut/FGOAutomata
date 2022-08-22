from time import sleep
from random import randint
from configparser import ConfigParser
from pynput.mouse import Button, Controller

SKILL_MARGIN = 10
SPEED = 1

CONFIG = ConfigParser()
CONFIG.read("config_2.ini")
MOUSE = Controller()

def load_values(group: str, subgroup: str) -> tuple[int]:
    return tuple([int(value) for value in CONFIG[group][subgroup].split()])

def is_inside(coords: tuple[int], area: tuple[int]) -> bool:
    return (area[0]<coords[0]<area[2]) and (area[1]<coords[1]<area[3])

#DEBUG 
DEBUG = True
def debug(s: str) -> None:
    if DEBUG: print(f"[DEBUG] {s}")

def mouse_click(x: int, y: int) -> None:
    MOUSE.position = (x,y)
    MOUSE.move(1,0)
    MOUSE.move(-1,0)
    MOUSE.press(Button.left)
    MOUSE.release(Button.left)
    debug(f"Clicked at {(x,y)}") 

def random_coord_inside(values: tuple()) -> tuple[int]:
    x = randint(values[0]+SKILL_MARGIN, values[2]-SKILL_MARGIN)
    y = randint(values[1]+SKILL_MARGIN, values[3]-SKILL_MARGIN)
    debug(f"Random coord generated at {(x,y)} from {values}. is inside? {is_inside((x,y), values)}")
    return (x,y)

def random_click_inside(values: tuple()) -> None:
    coords = random_coord_inside(values)
    mouse_click(coords[0], coords[1])

def servant_skill(servant: int, skill: int) -> None:
    coords = load_values(f"Servant {servant}", f"skill_{skill}")
    debug(f"Loaded coords {coords} from {servant = } {skill = }")
    random_click_inside(coords)

def main():
    for i in range(3):
        for j in range(3):
            sleep(SPEED)
            servant_skill(i,j)
if __name__ == "__main__":
    main()