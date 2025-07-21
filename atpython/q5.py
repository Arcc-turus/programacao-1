peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / altura**2

if imc >= 40:
    classificacao = "Obesidade Classe 3"
elif imc <= 39.9 and imc >= 35:
    classificacao = "Obesidade Classe 2"
elif imc <= 34.9 and imc >= 30:
    classificacao = "Obesidade Classe 1"
elif imc <= 29.9 and imc >= 25:
    classificacao = "Excesso de peso"
elif imc <= 24.9 and imc >= 18.5:
    classificacao = "Normal"
elif imc <= 18.5:
    classificacao = "Abaixo do peso"

print(f"Seu imc é {imc:.2f} e sua classificação é {classificacao}")