animales = {"elefante": ""}
agregar = {"perro" : "Bobby", "tigre": "Peepe", "mono": "homero"}

animales.update(agregar)
novos_animais = {{"elefante":"Trompi"}, {"delfin":"Manolo"}}

for nome in novos_animais:
    animales.update( novos_animais)
print(animales)
