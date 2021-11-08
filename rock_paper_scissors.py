import random as rm

'''Juego de piedra, papel o tijera contra la computadora'''

def game():

    usuario = int(input('''\nEscoge el numero de tu opcion:
    1. Piedra
    2. Papel
    3. Tijera
    '''))

    computadora = int(rm.choice([1,2,3]))

    if usuario == computadora:
        return 'Empate!'

    elif win_the_user(usuario, computadora):

        return 'Ganaste!'
    return 'Perdiste!'

def win_the_user(player,computer):

    #Piedra gana a tijera (1 > 3), tijera a papel (3 > 2) y papel a piedra (2 > 1)

    if ((player == 1 and computer == 3) or
        (player == 3 and computer == 2) or
        (player == 2 and computer == 1)):

        return True
    
    else:
        return False


print(game())