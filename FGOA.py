from random import randint, random
from configparser import ConfigParser
from time import sleep
import mouse

DEBUG = False
CONFIG = ConfigParser()


def read_config(config_file: str) -> None:
    """Reads config file located in the same or subsequent directories

    Args:
        config_file (str): Config file name/path
    """

    CONFIG.read(config_file)


def wait(time: float, min: float = 0.1, max: float = 0.5) -> None:
    """Halts program for some amout of time between [min, max]

    Args:
        time (float): Default time
        min (float, optional): Minimum time delay to add. Defaults to 0.1.
        max (float, optional): Maximum time delay to add. Defaults to 0.5.
    """

    sleep(time + (min + (max - min) * random()))


def load_values(group: str, subgroup: str = "coords") -> tuple[int]:
    """Loads values from the configuration

    Args:
        group (str): Parent node
        subgroup (str, optional): Child node . Defaults to "coords".

    Returns:
        tuple[int]: All the values returned from the config
    """

    return tuple([int(value) for value in CONFIG[group][subgroup].split()])


def debug(s: str) -> None:
    """Prints output with a custom format if global variable GLOBAL is True

    Args:
        s (str): String to output to stdout
    """

    if DEBUG:
        print(f"[DEBUG] {s}")


def set_debug(mode: bool) -> None:
    """Set global variable DEBUG to mode

    Args:
        mode (bool): If True all commands will show useful data regarding its use
    """

    global DEBUG
    DEBUG = mode


def mouse_click(x: int, y: int) -> None:
    """Simulate mouse click at (x,y) coordinates

    Args:
        x (int): Absolute x coordinate
        y (int): Absolute y coordinate
    """

    mouse.move(x, y)

    # Need to wait for mouse to move
    sleep(0.1)
    mouse.click()
    debug(f"Clicked at {(x,y)}")


def random_coord_inside(coords: tuple(), offset: int = 0) -> tuple[int]:
    """Generates a random coordinate inside some values that represent the boundaries of a square.

    Args:
        coords (tuple): Coordinates that represent the boundaries of a square e.i (x1, y1, x2, y2)
        offset (int, optional): Margin. Defaults to 0.

    Raises:
        ValueError: If offset is negative or less than the diameter of the boundaries

    Returns:
        tuple[int]: Random coordinate inside boundaries
    """

    if offset < 0:
        print("Offset cannot be less than 0")
        raise ValueError

    if offset > (coords[0] - coords[1]) or (coords[1] - coords[3]):
        print("Offset is greater than the difference of coordinates")
        raise ValueError

    x = randint(coords[0] + offset, coords[2] - offset)
    y = randint(coords[1] + offset, coords[3] - offset)
    debug(f"Random coord generated at {(x,y)} from {coords}")
    return (x, y)


def random_click_inside(bound: tuple()) -> None:
    """Clicks at a random coordinate inside some boundaries

    Args:
        bound (tuple): Boundaries of the click e.i (x1, y1, x2, y2)
    """

    coords = random_coord_inside(bound)
    mouse_click(coords[0], coords[1])
    debug(f"Clicked at {coords = }")


def servant_skill(servant: int, skill: int) -> None:
    """Uses a servant skill

    Args:
        servant (int): Index of the servant in the configuration file
        skill (int): Index of the skill in the configuration file
    """

    coords = load_values(f"Servant {servant}", f"skill_{skill}")
    random_click_inside(coords)
    debug(f"Loaded coords {coords} from {servant = } {skill = }")


def servant_NP(servant: int) -> None:
    """Uses a servant NP

    Args:
        servant (int): Index of the servant in the configuration file
    """

    coords = load_values(f"Servant {servant}", "np")
    random_click_inside(coords)
    debug(f"Clicked NP card of {servant = }")


def face_card(card: int) -> None:
    """Clicks a given face card

    Args:
        card (int): Index of the card in the configuration file
    """

    coords = load_values("Face cards", f"card_{card}")
    random_click_inside(coords)
    debug(f"Clicked face card")


def mystic_skill(skill: int) -> None:
    """Uses a mystic code skill

    Args:
        skill (int): Index of the skill in the configuration file
    """

    coords = load_values("Mystic code")
    random_click_inside(coords)
    debug(f"Clicked mystic code")

    # click skill
    coords = load_values("Mystic code", f"skill_{skill}")
    random_click_inside(coords)
    debug(f"Clicked mystic code {skill = }")


def exchange(servant_1: int, servant_2: int) -> None:
    """Exchanges two servants
    !!NOT IMPLEMENTED YET

    Args:
        servant_1 (int): Index of the servant position in the exchange menu in the configuration file
        servant_2 (int): Index of the servant position in the exchange menu in the configuration file
    """


def attack() -> None:
    """Clicks the attack button"""

    coords = load_values("Attack button")
    random_click_inside(coords)
    debug(f"Clicked the attack button")


def focus_enemy(enemy: int) -> None:
    """Clicks on an enemy

    Args:
        enemy (int): Index of the enemy in the configuration file
    """
    coords = load_values("Enemies", f"coord_{enemy}")
    random_click_inside(coords)
    debug(f"Clicked the {enemy = }")


def target_skill(servant: int) -> None:
    """Clicks on a servant in the target menu

    Args:
        servant (int): Index of the servant in the configuration file
    """
    coords = load_values(f"Servant {servant}", "target_skill")
    debug(f"Targeted skill to {servant = }")
    random_click_inside(coords)


def wait_next_move():
    """Waits until the next possible time to act NOT IMPLEMENTED YET"""
    pass
