from random import randrange as rd

def dado(n = int):
    l = []
    for i in range(n):
        l.append(rd(1,7))
    print(l)

n = int(input("quanta vezes você quer girar o dado? "))

print("o resultados que você tirou no dado foram:\n\n")
dado(n)
