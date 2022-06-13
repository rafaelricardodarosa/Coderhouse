grupo = {"Miguel", "Blanca", "Mario", "Andres"}
agregar = {"Ana", "Eric", "Ramon", "Marta", "David"}
eliminar = {"Mario", "Miguel", "David"}

grupo.update(agregar)

for nome in eliminar:
    grupo.discard(nome)
print(grupo)
