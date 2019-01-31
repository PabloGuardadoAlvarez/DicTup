def paso1():
    cad=input("Cadena:")
    subcad=input("Caracter:")

    if(subcad.find(cad) > -1):
        print("es subcadena")
    else:
        print("no es subcadena")

def paso2():
    cad=input("Cadena:")
    subcad=input("Caracter:")
    if(cad<subcad):
        print(cad)
    else:
        print(subcad)

paso2()