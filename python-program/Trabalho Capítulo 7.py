# Nome: Roger Viana Gonçalves de Alencar
# RM: 97540

# Capitulo 07 - "Advanced" concepts of algorithms and flowcharts for logic in decision making

anos = float(input("Tempo como fumante (em anos)......:"))
preco = float(input("Valor do maço....................:"))
quant = float(input("Quantidade de maços por dia.......:"))

valor = (((anos * 365) * preco ) * quant)

if valor <= 20000:
    print("Com o valor de {}, você poderia comprar um motinha vrummm".format(valor))
elif valor > 20000 and valor <= 50000:
    print("Com o valor de {}, você poderia comprar uma bela moto".format(valor))
else:
    print("Com o valor de {}, você poderia comprar um civic tunado".format(valor))
