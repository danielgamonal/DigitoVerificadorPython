from itertools import cycle

def DigitoVerificador():
    run = input("Introduzca su Run sin puntos ni DV: ")
    reversed_digits = map(int,reversed(str(run)))
    factors = cycle(range(2,8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    dv = ((-s) % 11)
    if dv == 10:
        dv= "k"
        print("Su Run con Digito Verificador es: "+str(run)+"-"+str(dv))
    else:
        print("Su Run con Digito Verificador es: "+str(run)+"-"+str(dv))

DigitoVerificador()