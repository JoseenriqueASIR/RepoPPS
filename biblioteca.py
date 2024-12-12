# Ejercico 1: Python 3.12.7

from unidecode import unidecode

lista_libros = []

libro_prueba = {"titulo": "El mago de Oz",
 "autor": "L. Frank Baum",
 "ISBN": "9788446053774",
 "stock": 5,
 "unidades_prestadas": 0,
 "puntuacion_media": 0,
 "lista_opiniones": {
     "usuario": "Paco47",
     "puntuacion": 4,
     "comentario": "Muy buen libro"
 } }

libro_prueba2 = {"titulo": "Una navidad muy fun, fun, fun",
 "autor": "Megan Maxwell",
 "ISBN": "9788408294399",
 "stock": 7,
 "unidades_prestadas": 0,
 "puntuacion_media": 0,
 "lista_opiniones": {
     "usuario": "Kiko77",
     "puntuacion": 3,
     "comentario": "Aceptable. Me lo esperaba mejor."
 } }

libro_prueba3 = {"titulo": "Guía del autoestopista galáctico",
 "autor": "Douglas Adams",
 "ISBN": "9788433927996",
 "stock": 4,
 "unidades_prestadas": 0,
 "puntuacion_media": 0,
 "lista_opiniones": {
     "usuario": "Mariano27",
     "puntuacion": 4,
     "comentario": "Un libro muy interesante."
 } }

lista_libros.append(libro_prueba)
lista_libros.append(libro_prueba2)
lista_libros.append(libro_prueba3)

def buscar_libro(cadena_busqueda):
    cadena_busqueda_decode = unidecode(cadena_busqueda)
    for libro in lista_libros:
        libro_decode = unidecode(libro["titulo"])
        if (libro["ISBN"] == cadena_busqueda):
            return libro
        elif cadena_busqueda_decode.lower() in libro_decode.lower():
            print(libro)
    return None

def unidades_disponibles(libro):
    return libro["stock"] - libro["unidades_prestadas"]

def mostrar_libro(libro):
    mostrar = buscar_libro(libro)
    if ( mostrar != None):
        print(f"Titulo: {mostrar['titulo']}, Autor: {mostrar['autor']}, ISBN: {mostrar['ISBN']}, Disponible: {unidades_disponibles(mostrar)} de {mostrar['stock']}, Puntuacion media: {mostrar['puntuacion_media']}")
    else:
         print("El libro buscado no existe")

def crear_libro(titulo, autor, isbn):
    buscado = buscar_libro(isbn)
    if buscado != None:
        buscado["stock"] += 1
        print(buscado)
    else:
        nuevo_libro = {
            "titulo": titulo,
            "autor": autor,
            "ISBN": isbn,
            "stock": 1,
            "unidades_prestadas": 0,
            "puntuacion_media": 0,
            "lista_opiniones": {}
        }
        lista_libros.append(nuevo_libro)
        print(nuevo_libro)

def prestar_libro(isbn):
    buscado = buscar_libro(isbn)
    if buscado != None:
        if buscado["stock"] < 1:
            print("No hay unidades disponibles para prestar.")
        else:
            buscado["unidades_prestadas"] += 1
            print(buscado)
    else:
        print("El libro buscado no existe.")

def devolver_libro(isbn):
    buscado = buscar_libro(isbn)
    if buscado != None:
        if buscado["unidades_prestadas"] < 1:
            print("No hay unidades prestadas por lo que no puedes devolver el libro.")
        else:
            buscado["unidades_prestadas"] -= 1
            print(buscado)
    else:
        print("El libro buscado no existe.")

def eliminar_libro(isbn):
    buscado = buscar_libro(isbn)
    if buscado != None:
        print("El libro a eliminar es: ", buscado)
        lista_libros.remove(buscado)
        print("Libro eliminado.")
        print("Lista de libros actualizada:")
        print(lista_libros)
    else:
        print("El libro buscado no existe.")

def devolver_opiniones(isbn):
    buscado = buscar_libro(isbn)
    if buscado != None:
        print(f"Las opiniones de este libro son: \nUsuario: {buscado['lista_opiniones']['usuario']}\nPuntuación: {buscado['lista_opiniones']['puntuacion']}\nComentario: {buscado['lista_opiniones']['comentario']}")
    else:
        print("El libro buscado no existe.")

# Puebas hardcodeadas para los ejercicios 2 y 3:

print("Pruebas hardcodeadas:")
print()
print("Búsqueda de un libro por ISBN:")
print(buscar_libro("9788433927996"))
print()

print("Búsqueda de un libro por título:")
buscar_libro("Galáctico")
print()

print("Mostar libro:")
mostrar_libro("9788433927996")
print()

print("Crear libro nuevo:")
crear_libro("Enciclopedia mundial de perros", "Isabelle Collin, Marie-Paule Daniels-Moulin, Claire Dupuis, Florence Desachy", "9781644618783")
print()

print("Crear libro existente:")
crear_libro("Una navidad muy fun fun fun", "Megan Maxwell", "9788408294399")
print()

print("Prestar libro:")
prestar_libro("9788408294399")
print()

print("Devolver libro:")
devolver_libro("9788408294399")
print()

print("Eliminar libro:")
eliminar_libro("9788408294399")
print()

print("Mostrar opiniones:")
devolver_opiniones("9788433927996")
print()

# Puebas con menú interactivo para el ejercicio 4.
print("Pruebas con menú interactivo:")
def opciones():
    print("[B]uscar libro.")
    print("[C]rear libro (indicando Título#Autor#ISBN13).")
    print("[P]restar libro.")
    print("[D]evolver libro.")
    print("[E]liminar libro.")
    print("Mostrar [O]piniones.")
    print("[S]alir.")

salir = False
while True:
    if salir:
        break
    opciones()
    opcion = input("Escribe tu opción: ").strip().upper()

    while opcion not in ["B", "C", "P", "D", "E", "O", "S"]:
        print("Opción incorrecta")
        opciones()
        opcion = input("Escribe tu opción: ")
        

    while opcion in ["B", "C", "P", "D", "E", "O", "S"]:
        if opcion == "S":
            print("Saliendo.")
            salir = True
            break
        elif opcion == "B":
            busqueda = input("Introduce el ISBN o el título del libro: ")
            print(buscar_libro(busqueda))
            break
        elif opcion == "C":
            libro = input("Introduce el título, autor y ISBN del libro: ")
            libro = libro.split("#")
            crear_libro(libro[0], libro[1], libro[2])
            break
        elif opcion == "P":
            isbn = input("Introduce el ISBN del libro a prestar: ")
            prestar_libro(isbn)
            break
        elif opcion == "D":
            isbn = input("Introduce el ISBN del libro a devolver: ")
            devolver_libro(isbn)
            break
        elif opcion == "E":
            isbn = input("Introduce el ISBN del libro a eliminar: ")
            eliminar_libro(isbn)
            break
        elif opcion == "O":
            isbn = input("Introduce el ISBN del libro para mostrar opiniones: ")
            devolver_opiniones(isbn)
            break
        else:
            break
    print()