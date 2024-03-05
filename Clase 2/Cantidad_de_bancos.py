'''Escribe un programa que, a partir de la cantidad de bancos de un aula y la cantidad de 
alumnos inscriptos para un curso, permita determinar si alcanzan los bancos existentes. 
De  no  ser  así,  informar  además  cuantos  bancos  sería  necesario  agregar.  El  usuario 
deberá  ingresar  por  teclado  tanto  la  cantidad  de  bancos  que  tiene  el  aula,  como  la 
cantidad de alumnos inscriptos para el curso. 
 
Ejercicio 5: Cálculo del salario 
A un trabajador le pagan según sus horas trabajadas y la tarifa está a un valor por hora. 
Si la cantidad de horas trabajadas es mayor a 40 horas, la tarifa por hora se incrementa 
en  un  50%  para  las  horas  extras.  Calcular  el  salario  del  trabajador  dadas  las  horas 
trabajadas y la tarifa. '''



cantidad_bancos = int(input("Ingrese la cantidad de bancos del aula: "))
alumnos_inscriptos = int(input("Ingrese la cantidad de alumnos inscriptos: "))

if cantidad_bancos >= alumnos_inscriptos:
    print("Los bancos existentes alcanzan para todos los alumnos.")
else:
    bancos_necesarios = alumnos_inscriptos - cantidad_bancos
    print("No hay suficientes bancos. Se necesitan agregar", bancos_necesarios, "bancos.")