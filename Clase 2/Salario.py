'''Crea un programa que solicite al usuario ingresar las horas trabajadas y el valor por hora. 
El programa deberá calcular el salario multiplicando las horas trabajadas por el valor por 
hora e imprimir el resultado.'''



horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
valor_por_hora = float(input("Ingrese el valor por hora: "))
salario = horas_trabajadas * valor_por_hora
print("El salario es:", salario)