def fatorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    print(f"o resultado do fatorial de {n} é igual a {r}")

n = int(input("escreva um número: "))
fatorial(n)