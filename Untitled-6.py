def es_bisiesto(anio):
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return True
    else:
        return False

anio = 2012

if es_bisiesto(anio):
    print(f"{anio} es un año bisiesto")
else:
    print(f"{anio} no es un año bisiesto")





fruta=
while len(frutas)<5:
    nuevaFruta=input('ingresa una fruta: ')
    if nuevaFruta in frutas:
        if len 
        print(`esta fruta ya existe huevonaso ingresa otro pendejo`)
        for frutas
    

    frutas=[]
while len(frutas)<5:
    nuevaFruta=input('ingresa una fruta: ')
    for fruta in frutas:
        if len(nuevaFruta) == len(fruta):
            print('misma longitud / ingresa otro')
    if nuevaFruta in frutas:
        print('Esta fruta ya existe / ingrese otra fruta: ')
    else:
        frutas.append(nuevaFruta)

def textoLargo(array):
    longitudTexto=0
    mostrarFruta=''
    for index in range(0,len(array)):
        if len(array[index]) > longitudTexto:
            longitudTexto=len(array[index])
            mostrarFruta=array[index]
    return mostrarFruta

print(textolargo(frutas))

