Lista1 = [1, 12, 123]
Lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

Lista1.append(1234)
Lista1.append("Hola")
Lista2.append("Adios")
Lista2.append(1234)
Lista3 = Lista1.pop()
Lista4 = Lista2.pop("Adios")
Lista4 = Lista2.pop("Hola")
Lista5 = Lista4 + Lista3

print(Lista5)
