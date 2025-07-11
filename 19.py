from random import randrange as rd

def jogo():
    m = rd(1, 101)
    while True:
        n = int(input("escreva um número natural de 1 até 100: "))
        if n == m:
            print("parabéns, você escolheu o número certo")
        elif n < m:
            print(f"{n} é menor que o número correto")
        else:
            print(f"{n} é maior que o número correto")

jogo()