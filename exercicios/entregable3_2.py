"""Escribí un programa que lea un número impar por teclado. 
Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente."""

numero1 = int(input("Digite un numero: "))

while True:
    numero = int( input( "Introduce un número par: "))
    if numero % 2 == 0:
        break
    print( "Error: número impar.")

print( "Número par introducido:", numero)


