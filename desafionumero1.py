# Crear un programa para calcular la nota final de un estudiante en base a dos examenes,
# los examenes cuentan con un porcentaje distinto de la nota final
# Nota1 cuenta como  el 40% de la nota final
# Nota2 cuenta como el 60% de la nota final

nota1 = int(input("Digite la nota del examen?"))
nota2 = int(input("Digite la nota del examen?"))
primera_nota = nota1*0.4
segunda_nota = nota2*0.6
nota_final = primera_nota+segunda_nota

print("La primera nota parcial es: {:.1f}, la segunda nota parcial es: {:.1f} y el promedio es:{:.1f}".format(primera_nota, segunda_nota, nota_final))