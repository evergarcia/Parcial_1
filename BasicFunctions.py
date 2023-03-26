from conn_MongoDB import db



def add_book():
    id =int(input("id: "))
    titulo = input("nombre del libro: ")
    autor = input("autor: ")
    pais = input("Pais: ")
    fecha_publicacion = int(input("Fecha de publicacion: "))
    ciudad = input("Nombre de la ciudad: ")

    libro ={
        "_id": id,
        "titulo": titulo,
        "autor": autor,
        "pais": pais,
        "fecha_publicacion":fecha_publicacion,
        "ciudad": ciudad
    }
    return libro

def consultar_libro_por_titulo(titulo):
    # buscar el libro por su título
    #libro = db.books.find_one({"titulo": titulo})
    libro = db.books.find_one({"titulo": titulo})
    # imprimir el resultado
    if libro:
        print(libro)
    else:
        print("El libro no fue encontrado.")


def update_book():
    id =int(input("id: "))
    titulo = input("nombre del libro: ")
    autor = input("autor: ")
    pais = input("Pais: ")
    fecha_publicacion = int(input("Fecha de publicacion: "))

    libro ={
        "_id": id,
        "titulo": titulo,
        "autor":autor,
        "pais":pais,
        "fecha_publicacion":fecha_publicacion
    }
    return libro


def update_libro():
    global libro
    print("menu de opciones")
    print("1. Modificar todo el documento")
    print("2. Modificar solo un elemento del documento")
    opcion = input("Opcion: ")

    if opcion =="1":
        titulo = input("nombre del libro: ")
        autor = input("Nombre del autor: ")
        pais = input("Pais: ")
        fecha_publicacion = int(input("Fecha: "))

        libro = {
            "titulo": titulo,
            "autor": autor,
            "pais": pais,
            "fecha_publicacion": fecha_publicacion
        }
        return libro
    elif opcion =="2":
        indice =input("Ingrese el valor del indice: ")
        valor =input("ingrese valor a modificar: ")
        libro = {indice:valor}
    return libro