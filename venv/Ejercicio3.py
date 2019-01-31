def paso1():
    tuplaNames = ("Pablo","Manuel","Pedro","Ismael")
    for i in range(0,len(tuplaNames)):
        print("Estimado " + tuplaNames[i])

def paso2():
    tuplaNames = ("Pablo", "Manuel", "Pedro", "Ismael")
    nombre=input("Nombre: ")
    repeticiones=input("Veces que repetimos: ")
    aux = ""
    for i in range(0,len(tuplaNames)):

        if(tuplaNames[i] == nombre):
            aux = tuplaNames[i]

    if(aux==""):
        print("No existe")

    for i in range(0,int(repeticiones)):
            print(aux)


def paso3():
    tuplaPablo = ("Pablo", "Hombre")
    tuplaPedro = ("Pedro", "Hombre")
    tuplaIsabel = ("Isabel", "Mujer")
    tuplaTodos = (tuplaPablo,tuplaPedro,tuplaIsabel)
    nombre=input("Nombre: ")

    for i in range(0,len(tuplaTodos)):

        print(str(tuplaTodos[i][2:1]))

        if(str(tuplaTodos[i][1:2]) == "('Hombre',)" and str(tuplaTodos[i][0:2] == nombre )):
                 print("Estimado " + nombre)
        else:
            print("Estimada" + nombre)




paso3()