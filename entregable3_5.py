"""Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras el 
número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra 
en la lista de números y notificarlo:

🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra 
en una lista (devuelve True o False)
"""

from ast import While


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

valor = int(input("Digite un valor entre 0 y 9: "))

