#hacer una funcion que muestre un nombre
#vamos a tener una lista de nombres
#por cada nombre en la lista se va a ejecutar la funcion
#todo esto tambien tenerlo en una funcion

lista = {
    "Arturo",
    "Melo",
    "Topi"
}

#por cada nombre llamar funcion que muetre el nombre

#la primer funcion va a tener nuestra lista y la logica para llamar la segunda funcion

#la segunda funcion va a imprimir un nombre

def lista_nombres():
    imprimir_nombre()

def imprimir_nombre():
    for nombre in lista:
        print(nombre)

lista_nombres()