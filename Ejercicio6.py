from random import randint
 
opc = ["piedra","papel","tijera","fin"]
def main():
    compu = opc[randint(0,2)]
 
    jugador = input("Captura piedra, papel o tijera....Captura -fin- para salir: ").lower()
    print("La computadora escogio: " + compu)
 
 
    if jugador == compu:
        print("EMPATE")
    elif jugador == "piedra" and compu == "papel":
        print("La computadora ganó")
    elif jugador == "piedra" and compu == "tijera":
        print("GANASTE")
    elif jugador == "papel" and compu == "piedra":
        print("GANASTE")
    elif jugador == "papel" and compu == "tijera":
        print("La computadora ganó")
    elif jugador == "tijera" and compu  == "piedra":
        print("La computadora ganó")
    elif jugador == "tijera" and compu == "papel":
        print("GANASTE")
    elif jugador == "fin":
        exit("Hasta luego")
        StopIteration
 
    main()
 
main()