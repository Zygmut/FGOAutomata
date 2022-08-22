from time import sleep
from FGOA import attack, servant_skill

def test_skills(times: int = 5):
    for t in range(times):
        for i in range(3):
            for j in range(3):
                servant_skill(i,j)

def test_attack_button(times: int = 5):
    for t in range(times):
        attack()
        sleep(0.5)

sleep(1)
test_attack_button(10)