nome = str(input("Digite seu nome completo;")).strip() #strip serve para eliminar espacos
print("Analisando seu nome...")
print("Seu nome em maiusculas é: {}".format(nome.upper())) #upper para colocar seu nome todo em maisculo
print("Seu nome em minusculo é: {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" "))) #len serve para contar qts letras e nomecount para contar espacos.

