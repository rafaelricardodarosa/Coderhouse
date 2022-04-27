""" Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:


1.	Mostrar una suma de los dos números
2.	Mostrar una resta de los dos números (el primero menos el segundo)
3.	Mostrar una multiplicación de los dos números
4.	Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
5.	En caso de no introducir una opción válida, el programa informará de que no es correcta.
"""
n1 = float( input( "Introduce el primer número: "))
n2 = float( input( "Introduce el segundo número: "))

while True:
    print("\nElige una opción:")
    print( "1.- Sumar dos números")
    print( "2.- Restar dos números")
    print( "3.- Multiplicar dos números")
    print( "4.- Salir")
    opcion = input( "Elige una opción (1-4): ")
    
    if opcion == '1':
        print( "La suma ", n1, "+", n2, "=", n1+n2)
    elif opcion == '2':
        print( "La resta ", n1, "-", n2, "=", n1-n2)
    elif opcion == '3':
        print( "La multiplicación ", n1, "*", n2, "=", n1*n2)
    elif opcion == '4':
        break
    else:
        print( "** Seleccion incorrecta **")



