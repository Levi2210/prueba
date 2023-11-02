# Definimos una función que suma dos números y devuelve el resultado
def suma(a, b):
    return a + b

# Definimos una función que resta dos números y devuelve el resultado
def resta(a, b):
    return a - b

# Definimos una función que multiplica dos números y devuelve el resultado
def multiplicacion(a, b):
    return a * b

# Definimos una función que divide dos números
# Si el divisor es cero, devuelve un mensaje de error; de lo contrario, devuelve el resultado
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

# Iniciamos un bucle infinito para que el usuario pueda realizar múltiples operaciones
while True:
    # Mostramos el menú de opciones al usuario
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    # Solicitamos al usuario que elija una opción
    opcion = input("Elige una opción (1/2/3/4/5): ")
    
    # Si el usuario elige la opción de salir, terminamos el bucle
    if opcion == "5":
        print("¡Hasta luego!")
        break

    # Si el usuario elige una opción válida (1 a 4)
    if opcion in ("1", "2", "3", "4"):
        # Solicitamos al usuario que ingrese dos números
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        # Realizamos la operación correspondiente según la opción elegida y mostramos el resultado
        if opcion == "1":
            print("Resultado: ", suma(num1, num2))
        elif opcion == "2":
            print("Resultado: ", resta(num1, num2))
        elif opcion == "3":
            print("Resultado: ", multiplicacion(num1, num2))
        elif opcion == "4":
            print("Resultado: ", division(num1, num2))
    else:
        # Si el usuario no elige una opción válida, mostramos un mensaje de error
        print("Opción no válida. Por favor, elige una opción válida (1/2/3/4/5).")
