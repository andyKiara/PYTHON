
alumnos = {}

alumnos["nombre"] = input("Ingrese el nombre del alumno: ")
alumnos["apellidos"] = input("Ingrese los apellidos del alumno: ")
alumnos["dni"] = input("Ingrese el DNI del alumno: ")
alumnos["programa_estudio"] = input("Ingrese el programa de estudio del alumno: ")

unidades_didacticas = []

num_unidades = int(input("Ingrese el número de unidades didácticas: "))

for i in range(num_unidades):
    unidad = {}
    nombre_unidad = input(f"Ingrese el nombre de la unidad {i+1}: ")
    promedio = float(input(f"Ingrese el promedio de la unidad {i+1}: "))

    if promedio >= 14:
        condicion = "aprobado"
    else:
        condicion = "desaprobado"

    unidad[nombre_unidad] = {"promedio": promedio, "condicion": condicion}
    unidades_didacticas.append(unidad)

alumnos["unidades_didacticas"] = unidades_didacticas

print(alumnos)
