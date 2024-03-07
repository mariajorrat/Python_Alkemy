'''
Consigna:
Argentina tiene, entre otros, los siguientes feriados siempre en las mismas fechas (inamovibles):
-Escriba un programa que lea el dia y mes que ingresa el Usuario.
-Si el mes y dia coinciden con alguno de los feriados listados previamente, entonces el programa debe mostrar el nombre del feriado.
-En otro caso, tu programa deberia indicar que para el dia y mes ingresado, no corresponde un feriado.

Paso a paso:
1.Declará las variables necesarias, asignales los valores correspondientes para ir probando el código
2.Construí tu primer estructura condicional para abordar esta verificación de datos
3.Aplicá los operadores que consideres necesarios para construir la lógica del condicional
4.Establecé un print() con el resultado final en todos los casos
'''

#1: Declaración de variables
# Valores de ejemplo para probar el código, sustituir con input() para leer valores reales del usuario
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes (en números): "))

# Diccionario que asocia (mes, dia) con el nombre del feriado
feriados = {
    (1, 1): "Año Nuevo",
    (5, 1): "Día del Trabajador",
    (5, 25): "Día de la Revolución de Mayo",
    (6, 20): "Día de la bandera",
    (7, 9): "Día de la Independencia",
    (12, 8): "Inmaculada Concepción de María",
    (12, 25): "Navidad"
}

#2: Estructura condicional
#3: Aplicación de operadores lógicos
#4: Print con el resultado
if (mes, dia) in feriados:
    print(f"El {dia}/{mes} es el feriado de {feriados[(mes, dia)]}.")
else:
    print(f"El {dia}/{mes} no corresponde a un feriado.")