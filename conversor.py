pesos = input("¿Cuántos pesos mexicanos tienes?: ")
pesos = float(pesos)
valor_dolar = 20.45
dolares = pesos/valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Usted tiene " + dolares + " dolares")

