from calendar import isleap

ano = int(input("Digite un año:"))

if isleap(ano):
    print('É bissexto')
else:
    print('Não é bissexto')