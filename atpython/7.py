t = input("escreva uma frase\n\n").lower()

v = ["a", "e", "i", "o", "u"]
t = t.split(" ")
r = 0

for i in range(0, len(t)):
    for b in range(0, len(t[i])): 
        a = t[i]
        if a[b] in v:
            r += 1

print(f"sua frase tem {r} vogais")
