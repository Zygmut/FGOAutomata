from pynput.mouse import Listener, Controller
from configparser import ConfigParser
import keyboard
import logging
import argparse

logging.basicConfig(
    encoding="utf-8",
    level=logging.DEBUG,
    format="[CC %(levelname)s] %(message)s ",
)

CONFIG = ConfigParser()


def on_click(x, y, button, pressed) -> bool:
    return pressed


def get_mouse_coords() -> tuple[int, int]:
    with Listener(on_click=on_click) as listener:
        mouse = Controller()
        listener.join()

    return mouse.position


def get_box_coords() -> tuple[int, int, int, int]:
    return get_mouse_coords() + get_mouse_coords()


def servant_skills() -> None:
    logging.info("Calibrating servant skills")

    for servant_num in range(3):
        logging.info(f"Calibrating servant {servant_num}")
        CONFIG[f"Servant {servant_num}"] = {}

        for skill_num in range(3):
            coords = get_box_coords()
            logging.debug(f"Skill {skill_num} at {coords}")

            CONFIG[f"Servant {servant_num}"][f"skill_{skill_num}"] = " ".join(
                map(str, coords)
            )


def target_skill() -> None:
    logging.info("Calibrating target skills")

    for servant_num in range(3):
        coords = get_box_coords()
        logging.debug(f"Servant {servant_num} at {coords}")

        CONFIG[f"Servant {servant_num}"]["target_skill"] = " ".join(map(str, coords))


def enemies() -> None:
    logging.info("Calibrating enemies")

    CONFIG["Enemies"] = {}

    for enemy_num in range(3):
        coords = get_box_coords()
        logging.debug(f"Enemy {enemy_num} at {coords}")
        CONFIG["Enemies"][f"coord_{enemy_num}"] = " ".join(map(str, coords))


def attack_button() -> None:
    logging.info("Calibrating attack button")

    CONFIG["Attack button"] = {}

    coords = get_box_coords()
    logging.debug(f"Attack button at {coords}")
    CONFIG["Attack button"]["coords"] = " ".join(map(str, coords))


def mystic_code() -> None:
    logging.info("Calibrating mystic code ")

    CONFIG["Mystic code"] = {}

    coords = get_box_coords()
    logging.debug(f"Mystic code coords at {coords}")
    CONFIG["Mystic code"]["coords"] = " ".join(map(str, coords))

    logging.info("Calibrating mystic code skills")
    for mc_skill_num in range(3):
        coords = get_box_coords()
        logging.debug(f"MC skill {mc_skill_num} at {coords}")
        CONFIG["Mystic code"][f"skill_{mc_skill_num}"] = " ".join(map(str, coords))


def mystic_code_exchange() -> None:
    logging.info("Calibrating Mystic code exchange")
    CONFIG["Exchange"] = {}

    for servant_num in range(6):
        coords = get_box_coords()
        logging.debug(f"Servant {servant_num} at {coords}")
        CONFIG["Exchange"][f"servant_{servant_num}"] = " ".join(map(str, coords))

    logging.info("Calibrating replace button")

    coords = get_box_coords()
    logging.debug(f"Replace button at {coords}")
    CONFIG["Exchange"]["replace"] = " ".join(map(str, coords))


def servant_face_cards() -> None:
    logging.info("Calibrating Face cards")

    CONFIG["Face cards"] = {}

    for card_num in range(5):
        coords = get_box_coords()
        logging.debug(f"Card {card_num} at {coords}")
        CONFIG["Face cards"][f"card_{card_num}"] = " ".join(map(str, coords))


def servant_np() -> None:
    logging.info("Calibrating NP cards")

    for servant_num in range(3):
        coords = get_box_coords()
        logging.debug(f"Card {servant_num} at {coords}")
        CONFIG[f"Servant {servant_num}"]["NP"] = " ".join(map(str, coords))


def calibrate(config_file="config.conf"):
    logging.info("Calibration procedure")
    calibrating = (
        servant_skills,
        servant_np,
        servant_face_cards,
        mystic_code,
        mystic_code_exchange,
        attack_button,
        enemies,
        target_skill,
    )

    CONFIG.read(config_file)

    for procedure in calibrating:
        logging.info(f"Next up is {procedure.__name__}, press ENTER to proceed ...")
        keyboard.wait("enter")
        procedure()

    with open(config_file, "w") as file:
        CONFIG.write(file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o", "--output", help="Output file", default="config.conf", type=str
    )
    args = parser.parse_args()

    calibrate(args.output)
