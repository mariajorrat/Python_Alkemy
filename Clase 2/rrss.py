'''
Consigna:
Una popular red social está implementando un filtro de edad obligatorio para sus nuevos usuarios, que verifica su edad, de acuerdo a la misma establece o no un control parental
-Si el usuario tiene menos de 12 años, no le permite crearse una cuenta
-Si el usuario tiene entre 13 y 17 años, le permite crearse una cuenta con control parental activado
-Si el usuario tiene 18 años o más, le permite crearse una cuenta sin restricciones

Bonus:
-Al mismo tiempo, en todos los casos, deberá haber facilitado su DNI para comprobar realmente la información, si no lo hizo, no puede hacerse ningún tipo de cuenta, sin importar su edad

Paso a paso:
1.Declará las variables necesarias, asignales los valores correspondientes para ir probando el código
2.Construí tu primer estructura condicional para abordar esta verificación de datos
3.Aplicá los operadores que consideres necesarios para construir la lógica del condicional
4.Establecé un print() con el resultado final en todos los casos
'''

import random

# Paso 1: Declaración de variables
edad_usuario = random.randint(1, 100)  # Asigna una edad aleatoria entre 1 y 100
dni_proveido = True  # Valor de ejemplo; establecer en función de si se ha proporcionado el DNI o no

# Imprimir la edad aleatoria asignada
print(f"Edad asignada al usuario: {edad_usuario}")

# Paso 2 y 3: Estructura condicional y lógica del condicional
if dni_proveido:
    if edad_usuario < 12:
        print("No se permite crear una cuenta debido a la edad.")
    elif 12 <= edad_usuario <= 17:
        print("Cuenta creada con control parental activado.")
    else:
        print("Cuenta creada sin restricciones.")
else:
    print("Debe proporcionar su DNI para verificar su edad.")