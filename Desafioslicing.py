nombre_alumno = input("Digite el nombre:")
nota = input("Digite la nota:")
materia = input("Digite la materia:")

nombre_volteada = nombre_alumno[::-1]
nota_volteada = nota[::-1]
materia_volteada = materia[::-1]

print("{} ha sacado un {} en {}".format(nombre_alumno,nota,materia))
print("{}, {}, {}".format(materia_volteada,nota_volteada,nombre_volteada))
