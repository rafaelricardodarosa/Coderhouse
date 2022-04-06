a = input("Digite algo!")
print("O tipo primitivo desse valor é:", type(a))
print("Só tem espacos?", a.isspace())
print("É um numero?", a.isnumeric())
print("É Alfabetico?", a.isalpha())
print("É alfanumerico?", a.isalnum())
#para checar se tudo esta em maisculo
print("Esta em maiscula?", a.isupper())
#para checar se esta tudo em minusculo
print("Esta em minusculo?", a.islower())
#para checar se tem maiusculas e minusculas
print("Esta capitalizada?", a.istitle())
