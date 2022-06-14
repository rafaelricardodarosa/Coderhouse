"""Escribí un programa que pida al usuario cuantos números 
quiere introducir. Luego lee todos los números y realiza una media aritmética:"""

numeros = int(input("Cuántos números quieres introducir? "))
lista = []

for x in range(numeros):
    n = int(input("Introduce un número: "))
    lista.append(n)

print("Tu introduciste: {} numeros y la media aritmetica de ellos es: {:1}".format(len(lista), sum(lista)/len(lista)))
