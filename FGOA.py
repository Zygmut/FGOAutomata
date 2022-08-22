from random import randint
from configparser import ConfigParser
from pynput.mouse import Button, Controller

SKILL_MARGIN = 10
SPEED = 1

CONFIG = ConfigParser()
CONFIG.read("config2.ini")
MOUSE = Controller()

def load_values(group: str, subgroup: str = "coords") -> tuple[int]:
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

def servant_NP(servant: int) -> None:
    coords = load_values("NP cards", f"card_{servant}")
    debug(f"Clicked face card at {coords = }")
    random_click_inside(coords)

def face_card(card: int) -> None:
    coords = load_values("Face cards", f"card_{card}")
    debug(f"Clicked face card at {coords = }")
    random_click_inside(coords)

def mystic_skill(skill: int) -> None:
    coords = load_values("Mystic code")
    debug(f"Clicked mystic code at {coords = }")
    random_click_inside(coords)
    
    # click skill
    coords = load_values("Mystic code", f"skill_{skill}")
    debug(f"Clicked mystic code skill at {coords = }")
    random_click_inside(coords)

def exchange(servant_1: int, servant_2: int) -> None:

    pass

def attack() -> None:
    coords = load_values("Attack button")
    debug(f"Clicked the attack button at {coords = }")
    random_click_inside(coords)

def focus_enemy(enemy: int) -> None:
    coords = load_values("Enemies", f"coord_{enemy}")
    debug(f"Clicked the {enemy = }")
    random_click_inside(coords)

def target_skill(servant: int) -> None:
    coords = load_values(f"Servant {servant}", "target_skill")
    debug(f"Targeted skill to {servant= }")
    random_click_inside(coords)

def wait_next_move():
    pass

def main():
    pass

if __name__ == "__main__":
    main()