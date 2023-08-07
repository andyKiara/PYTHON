#tendras que mostrar por consola, solo cuando encuentre el color rojo mostrara el mensaje de color encontrado y se termina la ejecucion

colores = ['azul', 'verde', 'amarillo', 'rojo', 'naranja']

for color in colores:
    print(color)
    if color == 'rojo':
        print('¡Color encontrado!')
        break
    