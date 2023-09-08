import FGOA
import random
from time import sleep

CASTORIA_LEFT = 0
SPISHTAR = 1
CASTORIA_RIGHT = 2


def random_atacks() -> tuple[int, int]:
    selected = random.randint(0, 3)
    return (selected, selected + 1)


def test():
    sleep(random.randint(0, 3))

    input("NExt run?")


def run() -> int:
    FGOA.wait_next_move()
    wait(2)

    FGOA.servant_skill(CASTORIA_LEFT, 2, SPISHTAR, True)
    FGOA.wait_next_move()

    FGOA.servant_skill(CASTORIA_RIGHT, 2, SPISHTAR, True)
    FGOA.wait_next_move()

    FGOA.servant_skill(SPISHTAR, 0, True)
    FGOA.wait_next_move()

    FGOA.attack()
    FGOA.servant_np(SPISHTAR)
    list(map(FGOA.face_card, random_atacks()))
    FGOA.wait_next_move()


if __name__ == "__main__":
    print(FGOA.run_battle(test, 10))
