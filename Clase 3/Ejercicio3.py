def aritmetica(opcion):
    if opcion == 1:
        # Acción A
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print("La suma de los números es:", resultado)
    elif opcion == 2:
        # Acción B
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = num1 * num2
        print("El producto de los números es:", resultado)
    else:
        print("Opción no válida")

opcion = int(input("Ingrese 1 para realizar la acción A o 2 para realizar la acción B: "))
aritmetica(opcion)