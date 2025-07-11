def palindromo(t = str):
    t2 = t[::-1]
    if t == t2:
        print(f"a palavra {t} é uma palavra palindroma\n")
    else:
        print(f"a palavra {t} não é uma palavra palindroma\n")

t = input("escreva uma palavra")
palindromo(t)
