nota = float(input("Digite su nota:"))

if nota >0 and nota <= 5.9:
    print("Su nota fue {} , esta desaprobado.".format(nota))
elif nota >= 6 and nota <=10:
    print("Su nota fue {}, esta aprobado.".format(nota))
elif nota <= 0 or nota > 10:
    print("Nota invalida, digite otra vez.")
