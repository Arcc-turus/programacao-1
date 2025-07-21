v = float(input("Total da compra: "))
p = float(input("Valor pago: "))

t = p - v

if t > 0:
    print(f"o seu troco será R${t}")
elif t < 0:
    print(f"ainda está faltando pagar R${-t}")
else:
    print("não tem troco")
