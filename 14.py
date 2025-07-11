def eh_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primos(n = int):
    if n >= 2:
        print(2)
    if n >= 3:
        print(3)        
    if n > 3:
        for e in range(4, n+1):
            if eh_primo(e) == True:
                print(e)


n = int(input("escreva um número maior de zero: "))
primos(n)
