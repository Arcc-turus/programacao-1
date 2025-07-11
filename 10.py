def maior(n1, n2, n3):
    l = []
    l.append(n1)
    l.append(n2)
    l.append(n3)
    l.sort()
    print(l[2])

n1 = int(input("escreva o primeiro número: "))
n2 = int (input("escreva o segundo número: "))
n3 = int (input("escreva o terceiro número número: "))

maior(n1, n2, n3)
