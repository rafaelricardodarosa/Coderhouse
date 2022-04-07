import math
co = float(input("Digite cateto oposto:"))
ca = float(input("Digite cateto Adjacente:"))
hi = math.hypot(co, ca)

print("A hipotenusa vai medir {:.2f}".format(hi))