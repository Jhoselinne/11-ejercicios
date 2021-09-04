#GUESS THE NUMBER/ADIVINA EL NUMERO RANDOM
import random

num = random.randint(1, 50)
guess = None

while guess != num:
    guess = input("Captura un numero entre 1 y 50: ")
    guess = int(guess)

    if guess == num:
        print("Felicidades ese es el numero!")
        break
    else:
        print("Incorrecto, Intenta de nuevo")