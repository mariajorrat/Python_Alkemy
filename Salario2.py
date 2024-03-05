'''A un trabajador le pagan según sus horas trabajadas y la tarifa está a un valor por hora. 
Si la cantidad de horas trabajadas es mayor a 40 horas, la tarifa por hora se incrementa 
en  un  50%  para  las  horas  extras.  Calcular  el  salario  del  trabajador  dadas  las  horas 
trabajadas y la tarifa. '''



# Entrada del usuario
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))

# Cálculo del salario
if horas_trabajadas > 40:
    horas_extras = horas_trabajadas - 40
    salario = (40 * tarifa_por_hora) + (horas_extras * tarifa_por_hora * 1.5)
else:
    salario = horas_trabajadas * tarifa_por_hora

# Imprimir el resultado
print(f"El salario total del trabajador es: {salario}")