# recibe un año por parametro
# imprima "el año es bisiesto
# imprima el año no es bisiesto
#si ingresa algo que no es numero debe de avisar

""" los años bisiesto son multiplos de 4, pero los multiplos de 100 no lo son
aunque  los multiplos de 400 si, 2012 bisiesto 2010 no es 2000 es bisiesto"""

ano = input("Ingrese el año: ")
if not ano.isdigit():
    print("No es un numero")
else:
    ano = int(ano)
    def es_bisiesto(ano):
        if ano % 4 == 0 and ano%100 != 0:
            return True
        elif ano%100 == 0 and ano%400 == 0:
            return print("El año {} es bisiesto".format(ano))
        else:
            return print("El año {} no es bisiesto".format(ano))
    es_bisiesto(ano)