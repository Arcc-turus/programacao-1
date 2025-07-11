def par(n):
    if n%2 != 0:
        return False
    else:
        return True
    
n = int(input("escreva um número inteiro: "))

if par(n) == True:
    print(f"o número {n} é par")
else:
    print(f"o número {n} é ímpar")
