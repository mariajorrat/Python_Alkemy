'''Escribe un programa que solicite al usuario ingresar el año actual y su año de nacimiento.
El programa deberá calcular la edad de la persona y mostrar el resultado.'''



current_year = int(input("Ingrese el año actual: "))
birth_year = int(input("Ingrese su año de nacimiento: "))

age = current_year - birth_year
print("Su edad es:", age)