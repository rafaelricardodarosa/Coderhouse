# Crear un programa para calcular la nota final de un estudiante en base a dos examenes,
# los examenes cuentan con un porcentaje distinto de la nota final
# Nota1 cuenta como  el 40% de la nota final
# Nota2 cuenta como el 60% de la nota final

nota_1 = int(10)
nota_2 = int(7)
nota_3 = int(4)
primera_nota = nota_1*0.15
segunda_nota = nota_2*0.35
tercera_nota = nota_3*0.5

nota_final = primera_nota+segunda_nota+tercera_nota

print("La primera nota parcial es: {:.1f}, la segunda nota parcial es: {:.1f}, la tercera nota parcial es:{:.1f} y el promedio es:{:.1f}".format(primera_nota, segunda_nota,tercera_nota, nota_final))