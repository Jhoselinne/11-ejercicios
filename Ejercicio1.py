#ODD OR EVEN/PAR E IMPAR

num = input("Captura un número: ")
num = int(num)

if num == 0:
    print ("El número capturado es par.")
elif num%2 == 0:
    print ("El número capturado es par")
else:
    print ("El número capturado es impar")