#Is a palindrome

palabra = input("Captura una palabra:")

if str(palabra) == str(palabra)[::-1]:
    print("La palabra SI es palindroma")
else:
    print("La palabra NO es palindroma")