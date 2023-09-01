import FGOA
import random
from time import sleep


def run() -> int:
    print("RUNNING")
    sleep(random.randint(1, 5))


if __name__ == "__main__":
    print(FGOA.run_battle(run, 10))
