# esta es una calculadora simple que suma , resta , multiplica y divide dos numeros.
#funcion para sumar dos numeros

def sumar(num1, num2):
    return num1 +num2

#funcion para restar dos numeros
def restar(num1, num2):
    return num1 - num2

#funcion para multiplicar dos numeros
def multiplicar(num1, num2):
    return num1 * num2

#funcion para dividir dos numeros 
def dividir(num1, num2):
    if num1 == num2:
        return "mal: No se puede dividir entre cero"
    else:
        return num1 / num2
    
    #Menu de la calculadora
    print("bienvenido a la calculadora mi king")
    print("seleccione una operacion")
    print("1. sumar")
    print("2, restar")
    print("3, multiplicar")
    print("4, dividir")
    
    # pide al usuario que ingrese dos numeros
    num1 = float(input("ingrese el primer numero: "))
    num2 =float (input("ingrese el segundo numero: "))

    # realiza la operacion seleccionada por el usuario e imprime el resultado
    if opcion == "1":
        print(num1, "+", num2, "=",
        sumar(num1,num2)) 

    elif opcion == "2":
     print(num1, "-", num2, "=",
           restar(num1,num2))
        
    elif opcion == "3":
        print(num1, "*", num2, "=",
              multiplicar(num1,num2))
        
    elif opcion == "4":
        print(num1, "==", num2, "=",
             dividir(num1,num2))
        
    else:
        print("opcion invalida")
        
        


