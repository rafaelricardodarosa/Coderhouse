def par_o_impar(numero):
    mensaje = f"El número {numero} es par" if numero % 2 == 0 else f"El número {numero} es impar"
    return mensaje
entrada = False
while entrada != 'q':
    entrada = input("Ingresar un valor númerico: ")
    try:
        print(par_o_impar(int(entrada)))
    except:
        print('¡Adios!') if entrada=='q' else print(f"[{entrada}] no es un número, para salir presione 'q'")