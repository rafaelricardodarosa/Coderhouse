import sys

print(sys.argv)
if len(sys.argv) < 3:
    print("No alcanzan los argumentos")
    exit()
try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
except:
    print("uno de los argumentos no es correcto")
    exit()
if num1 >= 7 and num2 >= 7:
    print("Promocionado")
elif num1 >= 7 or num2 >= 7:
    print("Aprobado")
elif num1 >= 4 and num2 >= 4:
    print("Reprobado")
else:
    print("Insuficiente")