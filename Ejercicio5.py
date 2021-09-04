#What's my acronym?/Acronimo de la frase

frase = input("Captura la institución: ")

texto = (frase.replace('of', '')).split()

acro = ""

for letra in texto:
    acro = acro + letra[0].upper()

print("El acronimo es:",acro)