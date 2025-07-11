l = []

while True:
    n = int(input("escreva um número: "))
    l.append(n)

    e = input("você quer colocar outro número na lista? \n").lower()
    if e[0] == "s":
        pass
    elif e[0] == "n":
        break

l = sorted(l)
lm = 0
for i in range(1, len(l) + 1):
    lm += i
lm = lm/len(l)

print(f"o maior número da lista é o número {l[0]}\no menor número da lista é o número {l[len(l)-1]}\na média dos números da lista é igual a {lm}")
