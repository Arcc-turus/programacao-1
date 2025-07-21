n = 0
s = 0

while True:
    n = int(input("escrva um número inteiro positivo: "))
    if n % 2 == 0:
        break
    print("escreva um númeor positivo.")

for i in range(2, n+1):
    if i % 2 == 0:
        s += i

print(f"a somas dos números pares até {n} é igual a {s}")
