from crud import*
from BasicFunctions import*

while True:
    print("Menu")
    print("1.Buscar libros por fecha")
    print("2.Buscar un libro por su titulo")
    print("3.Agregar un libro")
    print("4.Actualizar")
    print("5.Eliminar")
    print("6.Salir")

    opcion =input("Opcion: ")
    if opcion =="1":
        fecha = int(input("Ingrese fecha del libro: "))
        query_book_per_year(fecha)
        print("************************")
    elif opcion =="2":
        titulo = input("Ingrese el titulo del libro: ").lower()
        consultar_libro_por_titulo(titulo)
        print("Completado")
    elif opcion == "3":
        libro = add_book()
        create_book(libro)
        print("Completado")
    elif opcion =="4":
        id = int(input("Ingrese id del Libro: "))
        libro = update_libro()
        update_book(id,libro)
        print("Completado")
    elif opcion == "5":
        id = int(input("Ingrese el id del libro: "))
        if id is not None:
            confirmacion = input("¿Está seguro que desea eliminar el registro? (si/no): ").lower()
            if confirmacion == "si":
                delete_book(id)
            elif confirmacion == "no":
                print("cancelado.....")
        else:
            print("opcion no valida..")
        print("algo")
    elif opcion == "6":
        break
    else:
        print("Opción no valida")
