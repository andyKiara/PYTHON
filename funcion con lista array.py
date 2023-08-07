

def crear_lista_objetos(lista):
    lista_objetos = []
    for posicion, elemento in enumerate(lista):
        objeto = {
            'longitud': len(elemento),
            'nombre': elemento,
            'posicion': posicion
        }
        lista_objetos.append(objeto)
    return lista_objetos

lista = ["bosque", "vih", "bonorrea"]
lista_objetos = crear_lista_objetos(lista)
print(lista_objetos)

#crear una funcion que reciba como parametro de dos lista y retorne
un array de objetos  

def crear_lista_nombres(lista)
    crear_nombres =  []
    for edad, nombre 
    "nombre":nombre
