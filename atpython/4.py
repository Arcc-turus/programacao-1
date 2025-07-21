def maior(n1, n2, n3):
    l = [n1, n2, n3]
    l = sorted(l, reverse = True)
    return l[0]

n1 = float(input("escreva um número: "))
n2 = float(input("escreva outro número: "))
n3 = float(input("escreva outro número: "))

print(maior(n1, n2, n3))
