def senha_segura(s = str):
    maiusculo = False
    minusculo = False
    numero = False

    if len(s) < 8:
        return False
    
    for i in s:
        if i.isupper():
            maiusculo = True
        elif i.islower():
            minusculo = True
        elif    i.isdigit():
            numero = True

    if  maiusculo and minusculo and numero:
        return True
    else:
        return False

s = input("escreva a sua senha: ")

if senha_segura(s):
    print("\nSua senha é considerada segura.")
else:
    print("\nSua senha não é segura. Lembre-se que ela precisa ter no mínimo 8 caracteres, com letras maiúsculas, minúsculas e números.")
    