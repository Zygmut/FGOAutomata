from time import sleep
from random import randint
from pynput.mouse import Button, Controller
import logging

mouse = Controller()

logging.basicConfig(
    encoding="utf-8",
    level=logging.DEBUG,
    format="[MC %(levelname)s] %(message)s ",
)


def mouse_click(coords: tuple[int, int]) -> None:
    """Simulate mouse click at the passed coordinates

    Args:
        coords (tuple[int, int]): x and y coordinates
    """
    mouse.position = coords
    sleep(0.1)
    mouse.click(Button.left)
    logging.debug(f"Clicked at {coords}")


def __random_coord_inside(
    coords: tuple[int, int, int, int], offset: int = 10
) -> tuple[int, int]:
    """Generates a random coordinate inside some values that represent the
    boundaries of a square.

    Args:
        coords (tuple): Coordinates that represent the boundaries of a square
        e.i (x1, y1, x2, y2)
        offset (int, optional): Margin. Defaults to 0.

    Raises:
        ValueError: If offset is negative or less than the diameter of the
        boundaries

    Returns:
        tuple[int]: Random coordinate inside boundaries
    """

    if offset < 0:
        logging.error("Offset cannot be less than 0")
        raise ValueError

    if offset > ((abs(coords[0] - coords[1])) or (abs(coords[1] - coords[3]))):
        logging.error("Offset is greater than the difference of coordinates")
        raise ValueError

    if (coords[0] + offset) < (coords[2] - offset):
        x = randint(coords[0] + offset, coords[2] - offset)
    else:
        x = randint(coords[2] - offset, coords[0] + offset)

    if (coords[1] + offset) < (coords[3] - offset):
        y = randint(coords[1] + offset, coords[3] - offset)
    else:
        y = randint(coords[3] - offset, coords[1] + offset)

    logging.debug(f"Random coord generated at {(x,y)} from {coords}")
    return (x, y)


def random_click_inside(bound: tuple[int, int, int, int]) -> None:
    """Clicks at a random coordinate inside some boundaries

    Args:
        bound (tuple[int,int,int,int]): Boundaries of the click e.i (x1, y1, x2, y2)
    """

    mouse_click(__random_coord_inside(bound))


def click_around(x_coord: int, y_coord: int, radius: int = 100) -> None:
    """Clicks around the point (x,y)

    Args:
        x (int): Absolute x coordinate
        y (int): Absolute y coordinate
        radius (int, optional): Dimension of the space created to click.
        Defaults to 100.
    """
    random_click_inside(
        (x_coord - radius, y_coord + radius, x_coord + radius, y_coord - radius)
    )
