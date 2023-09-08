from random import random
from configparser import ConfigParser
from time import sleep
from PIL import ImageGrab
from typing import Callable
import numpy as np
import cv2
import time
import logging

from mouse_controller import random_click_inside, click_around

CONFIG = ConfigParser()

logging.basicConfig(
    encoding="utf-8",
    level=logging.DEBUG,
    format="[FGOA %(levelname)s] %(message)s ",
)


def wait(time: float = 0, min_val: float = 0.1, max_val: float = 0.5) -> None:
    """Halts program for some amout of time between [min, max]

    Args:
        time (float): Default time
        min (float, optional): Minimum time delay to add. Defaults to 0.1.
        max (float, optional): Maximum time delay to add. Defaults to 0.5.
    """

    sleep(time + (min_val + (max_val - min_val) * random()))


def __load_values(group: str, subgroup: str = "coords") -> tuple[int, int, int, int]:
    """Loads values from the configuration

    Args:
        group (str): Parent node
        subgroup (str, optional): Child node . Defaults to "coords".

    Returns:
        tuple[int]: All the values returned from the config
    """

    return tuple(map(int, CONFIG[group][subgroup].split()))


def servant_skill(servant: int, skill: int, target: int = None, fast: bool = False) -> tuple[int, int]:
    """Uses a servant skill

    Args:
        servant (int): Index of the servant whos skills is being casted in the configuration file
        skill (int): Index of the skill in the configuration file
        target (int): Index of the servant who the skill is being targeted in the configuration file. Defaults to None
        fast (bool): Wheter to click again as to enable the "fast animation" system. Defaults to False

    Returns:
        tuple[int, int]: Clicked point
    """

    logging.debug(f"Clicking {skill = } from {servant = }")
    last_click = random_click_inside(__load_values(f"Servant {servant}", f"skill_{skill}"))

    if target:
        last_click = target_skill(target)

    if fast:
        click_around(*last_click)

    return last_click


def servant_np(servant: int) -> tuple[int, int]:
    """Uses a servant NP

    Args:
        servant (int): Index of the servant in the configuration file

    Returns:
        tuple[int, int]: Clicked point
    """

    logging.debug(f"Clicking NP card of {servant = }")
    return random_click_inside(__load_values(f"Servant {servant}", "np"))


def face_card(card: int) -> tuple[int, int]:
    """Clicks a given face card

    Args:
        card (int): Index of the card in the configuration file

    Returns:
        tuple[int, int]: Clicked point
    """

    logging.debug(f"Clicking face {card = }")
    return random_click_inside(__load_values("Face cards", f"card_{card}"))


def mystic_code() -> tuple[int, int]:
    """Clicks the mystic code menu
    TODO: test

    Returns:
        tuple[int, int]: Clicked point
    """

    logging.debug("Clicking mystic code")
    return random_click_inside(__load_values("Mystic code"))


def mystic_skill(skill: int) -> tuple[int, int]:
    """Uses a mystic code skill
    TODO: test

    Args:
        skill (int): Index of the skill in the configuration file

    Returns:
        tuple[int, int]: Clicked point
    """

    logging.debug(f"Clicking mystic code {skill = }")
    return random_click_inside(__load_values("Mystic code", f"skill_{skill}"))


def exchange(servant_1: int, servant_2: int) -> None:
    """Exchanges two servants
    TODO: test

    Args:
        servant_1 (int): Index of the servant position in the exchange menu in
        the configuration file
        servant_2 (int): Index of the servant position in the exchange menu in
        the configuration file
    """

    logging.debug(f"Clicking {servant_1 = } in the exchange menu")
    random_click_inside(__load_values("Exchange", f"servant_{servant_1}"))
    wait()

    logging.debug(f"Clicking {servant_2 = } in the exchange menu")
    random_click_inside(__load_values("Exchange", f"servant_{servant_2}"))
    wait()

    logging.debug("Clicking the replace button")
    random_click_inside(__load_values("Exchange", "replace"))


def attack() -> tuple[int, int] :
    """
    Clicks the attack button

    Returns:
        tuple[int, int]: Clicked point
    """

    logging.debug("Clicking the attack button")
    return random_click_inside(__load_values("Attack button"))


def focus_enemy(enemy: int) -> tuple[int, int]:
    """Clicks on an enemy
    TODO: test
    Args:
        enemy (int): Index of the enemy in the configuration file

    Returns:
        tuple[int, int]: Clicked point
    """

    logging.debug(f"Clicking the {enemy = }")
    return random_click_inside(__load_values("Enemies", f"coord_{enemy}"))


def target_skill(servant: int, fast: bool = False) -> tuple[int, int]:
    """Clicks on a servant in the target menu

    Args:
        servant (int): Index of the servant in the configuration file
        fast (bool): Wheter to click again as to enable the "fast animation" system. Defaults to False

    Returns:
        tuple[int, int]: Clicked point
    """

    logging.debug(f"Targeting skill to {servant = }")
    last_click = random_click_inside(__load_values(f"Servant {servant}", "target_skill"))

    if fast:
        logging.debug("Enabling fast animation")
        click_around(*last_click)

    return last_click


def locate_on_screen(img_path: str, coeff: float = 0.9) -> tuple[int] | None:
    """Generic method that detects if an image is visible onscreen

    Args:
        img_path (str): Path of the iamge to locate
        coeff (float, optional): Coefficient of validation. Defaults to 0.9.

    Returns:
        tuple[int] | None: Tuple containing the location of the image or None
        if not acquired
    """

    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    screenshot = cv2.cvtColor(np.array(ImageGrab.grab()), cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot, img, cv2.TM_CCOEFF_NORMED)
    _, disp_coeff, _, max_loc = cv2.minMaxLoc(result)
    if disp_coeff >= coeff:
        return max_loc
    else:
        return None


def wait_next_move(min_coeff=0.9) -> None:
    """Waits until the next possible time to act SOON TO BE DEPRECATED"""

    attack_img = cv2.imread("images/combat/menu.png", cv2.IMREAD_GRAYSCALE)

    coeff = 0

    # Image should be at 20 FPS
    while coeff < min_coeff:
        screenshot = cv2.cvtColor(np.array(ImageGrab.grab()), cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screenshot, attack_img, cv2.TM_CCOEFF_NORMED)
        _, coeff, _, _ = cv2.minMaxLoc(result)

    logging.debug("Menu found")


def run_battle(
    run_function: Callable,
    times: int = 1,
    config_file: str = "config.conf",
) -> list[int]:
    """Run wrapper

    Args:
        run_function (Callable): A function that describes what to do in a run
        times (int, optional): Amount of times to run each function. Defaults to 1.
        config_file (str, optional): Path to the config file. Defaults to "config.conf".

    Returns:
        list[int, ...]: All the times fetched from the execution
    """

    CONFIG.read(config_file)

    run_times = []

    for run_num in range(times):
        print(f"=== Run {run_num} ===")

        start_time = time.time()
        run_function()
        elapsed_time = int(time.time() - start_time)
        run_times.append(elapsed_time)

        print(f"Run {run_num} used {elapsed_time} seconds")
        print(
            f"Average time for each run = {sum(run_times)/len(run_times):.2f}",
            end="\n\n",
        )

    return run_times
