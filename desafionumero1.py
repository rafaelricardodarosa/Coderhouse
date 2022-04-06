# Crear un programa para calcular la nota final de un estudiante en base a dos examenes,
# los examenes cuentan con un porcentaje distinto de la nota final
# Nota1 cuenta como  el 40% de la nota final
# Nota2 cuenta como el 60% de la nota final

nota1 = int(input("Digite la nota del examen?"))
nota2 = int(input("Digite la nota del examen?"))
primeranota = nota1*0.4
segundanota = nota2*0.6
notafinal = primeranota+segundanota

print("La primera nota parcial es: {}".format(primeranota))
print("La Segunda nota parcial es:{}".format(segundanota))
print("La nota final del año es:{}".format(notafinal))