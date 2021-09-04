#EMAIL SLICER

correo = input("Captura tu correo: ").strip()

usuario = correo[:correo.index('@')]
dominio = correo[correo.index('@') + 1:]

print("Hola!\nTu usuario es:",usuario,"\nTu dominio es:",dominio)