import collections

from conn_MongoDB import*



def query_book_per_year(fecha):
    # buscar todos los libros con el año de publicación especificado
    libros = db.books.find({"fecha_publicacion": fecha})

    # imprimir los resultados
    for libro in libros:
        print(libro)


def create_book(libro):
    result =collections.insert_one(libro)
    print(result.inserted_id)

def update_book(id,json_indices_values):
    query ={"_id":id}
    new_values ={"$set": json_indices_values}
    result =collections.update_one(query,new_values)
    print(result.modified_count)

def delete_book(id=None):
    if id is not None:
        query = {"_id": id}
        result = collections.delete_one(query)
        print("se elimino...")
    else:
        print("no se encontro registro")

