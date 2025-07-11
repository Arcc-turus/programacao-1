def q_v(t = str):
    t = t.lower()
    vogais = ["a", "e", "i", "o", "u"]
    q = 0
    for i in range(len(t)):
        if t[i] in vogais:
            q += 1
    return q        

t = input("escreva uma palavra ou frase\n")
print(f"sua frase tem um total de {q_v(t)} vogais")
