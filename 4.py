def media(n1 = 0, n2 = 0, n3 = 0):
    m = (n1+n2+n3)/3
    return m

n1 = int(input("escreva um número inteiro: "))
n2 = int(input("escreva oto número inteiro: "))
n3 = int(input("escreva oto número inteiro: "))

print(f"a média entre os números {n1}, {n2} e {n3} é igual a {media(n1, n2, n3)} ")
