#hacer una funcion que muestre un nombre
#vamos a tener una lista de nombres
#por cada nombre en la lista se va a ejecutar la funcion
#todo esto tambien tenerlo en una funcion

#por cada nombre llamar funcion que muetre el nombre

#la primer funcion va a tener nuestra lista y la logica para llamar la segunda funcion

#la segunda funcion va a imprimir un nombre

def mostrar_nombre(nombre):
    print(nombre)

def nombres():
    lista = [
        "Arturo",
        "Melo",
        "Topi"
    ]

    for nombre in lista:
        mostrar_nombre(nombre)

nombres()