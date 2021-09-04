#Lyrics generator

def main():

    opc=int(input("Escoge una canción:\n1-Vida de rico de Camilo\n2-I Choose de Alessia Cara\n3-If I Ain't Got You de Alicia Keys\n4-Limón y Sal de Julieta Venegas\n5-Salir\n\n"))

    if opc == 1:
        print("Yo puedo ofrecerte una vida muy interesante\nPero depende para ti qué es interesante\nSi estás pensando en discotecas, carros y diamantes\nEntonces puede que pa ti sea insignificante")

    if opc == 2:
        print("All of my life\nI thought I was right\nLooking for something new\nStuck in my ways\nLike old-fashioned days\nBut all the roads led me to you")

    if opc ==3:
        print("Some people live for the fortune\nSome people live just for the fame\nSome people live for the power, yeah\nSome people live just to play the game")

    if opc ==4:
        print("Yo te quiero con limón y sal\nYo te quiero tal y como estás\nNo hace falta cambiarte nada\nYo te quiero si vienes o si vas\nSi subes, si bajas, si no estás\nSeguro de lo que sientes")
        
    if opc == 5:
        exit("Hasta luego")
        StopIteration
    main()
 
main()