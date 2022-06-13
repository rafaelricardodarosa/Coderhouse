class Perro():
    tipo = "Mamiferos"
    def __init__(self,nombre_perro,edad_perro):
        self.nombre = nombre_perro
        self.edad = edad_perro

perro1 = Perro("gordo",3)
perro2 = Perro("Ema",7)

print("mi pRIMERA mascota es,",perro1.nombre, "y tiene", perro1.edad, "años")