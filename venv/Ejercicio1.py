def paso1():

    cad=input("Cadena:")
    caracter=input("Caracter:")
    print(caracter.join(cad))

def paso2():
    cad = input("Cadena: ")
    print(cad.replace(" ","_"))

def paso3():
    cad = input("Cadena: ")
    caracter = input("Caracter:")
    for i in range(10):
        cad = cad.replace(str(i),caracter)
    print(cad)

def paso4():
    cad = input("Cadena: ")
    caracter = input("Caracter:")
    aux = ""
    for i in range(0,len(cad)):
        if(i%3==0 and i > 0):
           aux = aux + caracter
        aux = aux + cad[i]

    print(aux)

paso3()
