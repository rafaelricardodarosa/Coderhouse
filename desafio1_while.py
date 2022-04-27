lista = []

numero = int(input("Ingresa tu número: "))

while numero != 0:
    lista.append(numero)
    numero = int(input("Ingresa tu número: "))
    
print(lista)
suma_total = sum(lista)
print("la suma es: ", suma_total)
    