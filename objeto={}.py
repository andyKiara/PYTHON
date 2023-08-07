objeto={}
objeto["nombre"]=input("ingrese su nombre: ")
objeto["apellido"]=input("ingrese su apellido: ")
objeto["edad"]=int(input("ingrese su edad: "))
objeto["sexo"]=input("ingrese M si es masculino y F si es femenino: ")
print(objeto)


objeto[]
lista=
while len(lista)


#ALGORITMOS DE BUSQUEDA
#bubble sort
#insertion sort
#merge sort
#quick sort
#selection sort
#binary shearch tree


#UN PROGRAMA QUE ALAMACENE DATOS DE UNA EMPRESA CONE EL SIGUIENTE FORMATO
empresa = {
    'nombre': 'jory sac',
    'ruc': 123456789,
    'direccion': 'putaccasa s/n',
    'sucursales': ['uraluma', 'breapampa', 'pampapispa'],
    'horario': {
        'dia': '7-12',
        'tarde': '3-6'
    }
}

print(empresa)


empresa={}
empresa["nombre"]=input("ingrese el nombre de la empresa : ")
empresa["ruc"]=int(input("ingrese su ruc "))
empresa["direccion"]=int(input("ingrese su direccion ")),
while len(empresa["sucursales"])<2:
    sucursal=input("ingresa el nombre de la sucursal")
    empresa["sucursales"].append(sucursal)
empresa["horario"]={}
empresa["horario"]["dia"]=input("ingrese el horario del dia")
empresa["horario"]["tarde"]=input("ingrese el horario de la tarde")

print(empresa)




nombre=input("ingrese el nombre de la empresa: ")
ruc=input("ingrese el ruc: ")
direccion=input("ingrese direccion: ")
sucursal1=input("ingrese la primera sucursal: ")
sucursal2=input("ingrese la primera sucursal: ")
sucursal3=input("ingrese la primera sucursal: ")
empresa{"nombre":nombre,
        "ruc":ruc,
        "direccion":direccion,
        "sucursales":[sucursal1,sucursal2,sucursal3]
        "horario":{
            "dia":,
            "tarde:"
        }}



nombre=input("ingrese el nombre de la empresa: ")
ruc=input("ingrese el ruc: ")
direccion=input("ingrese direccion: ")
sucursales=input("ingrese sucursales separado por comas: ").
split(",")
horario_dia=input("ingrese el horario de dia: ")
horario_tarde=input("ingrese el horario de la tarde: ")
empresa=:{"nombre":nombre,
         "ruc":ruc,
          "direccion":direccion,
           "sucursales":sucursales,
            "horario":¨{
            "dia":horario_dia,
            "tarde":horario_tarde,
            }}


lista[2,5,0,4,1]
#crear una funcion que reciba como parametro una lista -> array y 



#·[{longitud:6,nombre:"bosque",posicion:0},]

def crear_lista_objetos(lista):
    lista_objetos = []
    for elemento in lista:
        objeto = {
            'caracteristica': elemento
        }
        lista_objetos.append(objeto)
    return lista_objetos

lista = ["bosque", "vih", "bonorrea"]
lista_objetos = crear_lista_objetos(lista)
print(lista_objetos)