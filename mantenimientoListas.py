from mailbox import NoSuchMailboxError
from re import I
from tkinter import SW
from asyncio.windows_events import NULL
from email.errors import MessageError
from socket import MsgFlag
from tokenize import String

list_art = []
nom_art = {}
desc_art = {}
precio_art = {}

# 2Se encarga de comprobar si el articulo esta(0) o si no esta(1) en la lista
def comprobarCod(pCod_art):
    aux = 1
    if pCod_art in list_art:
        aux = 0

    return aux

# Funcion para anadir un producto
def addProduct(pCod_art, pNom_art, pDesc_art, pPrecio_art):
    if comprobarCod(pCod_art) == 1:
        list_art.append(pCod_art)
        nom_art = {pCod_art : pNom_art}
        desc_art = {pCod_art : pDesc_art}
        precio_art = {pCod_art : pPrecio_art}
        print("Añadido.")
    else:
        print("Ya existe un producto con ese codigo de artículo")

# Funcion para eliminar un producto
def delProduct(pCod_art):
    if comprobarCod(pCod_art) == 0:
        list_art.pop(pCod_art)
        nom_art.pop(pCod_art)
        desc_art.pop(pCod_art)
        precio_art.pop(pCod_art)
        print("Borrado.")
    else:
        print("El producto no existe")
    
# Funcion para modificar un producto
def modProduct(pCod_art, pNom_art, pDesc_art, pPrecio_art):
    if comprobarCod(pCod_art) == 0:
        delProduct(pCod_art)
        addProduct(pCod_art, pNom_art, pDesc_art, pPrecio_art)
        print("Producto modificado")
    else:
        print("El producto a modificar no existe")

# Funcion para mostrar un producto
def showProduct(pCod_art):
    if comprobarCod(pCod_art) == 0:
        print("Codigo: " + str(pCod_art) + "\nNombre: " + str(nom_art[pCod_art]) + "\nDesc: " + str(desc_art[pCod_art]) + "\nPrecio: " + str(precio_art[pCod_art]))
    else:
        print("El producto a mostrar no exixste")

# Funcion para listar todos los articulos
def listProducts():
    for i in list_art:
        showProduct(i)
        print("\n\n")


# Menu para la interaccion del usuario1

exit = True

while exit:

    print("1: Añadir\n2: Borrar\n3: Modificar\n4: Búsqueda\n5: Listado\n0: Salir")
    res = int(input("-->"))

    if res == 1 :
        cod_art = int(input("Introduce el codigo del articulo: "))
        nom_art = input("Introduce el nombre del articulo: ")
        desc_art = input("Introduzca una breve descripcion del articulo: ")
        precio_art = input("Introduzca el precio del articulo: ")
        addProduct(cod_art, nom_art, desc_art, precio_art)
    elif res == 2 :
        delProduct(input("Introduce el codigo del producto a borrar:"))
    elif res == 3 :
        cod_art = int(input("Introduce el codigo del articulo a modificar: "))
        nom_art = (input("Introduce el nombre del articulo a modificar: "))
        desc_art = (input("Introduzca una breve descripcion del articulo a modificar: "))
        precio_art = ((input("Introduzca el precio del articulo a modificar: ")))
        modProduct(cod_art, nom_art, desc_art, precio_art)
    elif res == 4 :
        showProduct(int(input("Introduce el codigo del articulo a mostrar: ")))
    elif res == 5 :
        input("Lista de articulos: ")
        listProducts()
    elif res == 0:
        exit = False
    else:
        print("Solo opciones del 0 al 5")