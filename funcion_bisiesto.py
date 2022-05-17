# recibe un año por parametro
# imprima "el año es bisiesto
# imprima el año no es bisiesto
#si ingresa algo que no es numero debe de avisar

""" los años bisiesto son multiplos de 4, pero los multiplos de 100 no lo son
aunque  los multiplos de 400 si, 2012 bisiesto 2010 no es 2000 es bisiesto"""

año = int(input("Ingrese el año: "))

def es_bisiesto(año):
    if año % 4 == 0 and año%100 != 0:
        return True
    elif año%100 == 0 and año%400 == 0:
        return print("El año {} es bisiesto".format(año))
    else:
        return print("El año {} no es bisiesto".format(año))

es_bisiesto(año)