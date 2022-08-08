def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Usted tiene" + dolares + " dolares.")

menu = """
Bienvenido al conversor de monedas 🥵

1- Pesos mexicanos
2- Pesos colombianos 
3- Pesos argentinos

Elige una opción: """


opcion = int(input(menu))

if opcion == 1:
    conversor("mexicanos", 20)
elif opcion == 2:
    conversor("colombianos", 4345)
elif opcion == 3:
    conversor("argentinos", 133.47)
else:
    print("Ingresa una opción correcta, mamón.")



