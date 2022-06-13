Lista1 = [1, 12, 123]
Lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

Lista1.append(1234)
Lista1.append("Hola")
print(Lista1)

Lista2.append("Adios")
Lista2.append(1234)
print(Lista2)

Lista1.pop()
Lista2.pop()
Lista2.pop(0)
Lista3 = Lista1
Lista4 = Lista2
print(Lista3)
print(Lista4)

Lista5 = Lista3 + Lista4
print(Lista5)