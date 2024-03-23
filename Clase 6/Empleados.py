from enum import Enum
from datetime import datetime

class Categoria(Enum):
    FIJO = 1
    COMISION = 2

class Empleado:
    def __init__(self, dni, nombre, apellido, anio_ingreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso

    def salario(self):
        pass

class EmpleadoFijo(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, sueldo_basico):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.sueldo_basico = sueldo_basico

    def salario(self):
        anios = datetime.now().year - self.anio_ingreso
        if anios < 2:
            return round(self.sueldo_basico, 2)
        elif 2 <= anios <= 5:
            return round(self.sueldo_basico * 1.05, 2)
        else:
            return round(self.sueldo_basico * 1.10, 2)

class EmpleadoComision(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, salario_minimo, clientes_captados, monto_por_cliente):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente

    def salario(self):
        return round(max(self.salario_minimo, self.clientes_captados * self.monto_por_cliente), 2)

def mostrarSalarios(empleados):
    for empleado in empleados:
        print(f'{empleado.nombre} {empleado.apellido}: ${empleado.salario()}')

def empleadoConMasClientes(empleados):
    max_clientes = max((e for e in empleados if isinstance(e, EmpleadoComision)), key=lambda e: e.clientes_captados, default=None)
    if max_clientes:
        return max_clientes.nombre, max_clientes.apellido
    else:
        return "N/A", "N/A"

def ingresar_datos_empleado():
    dni = input("Ingrese DNI: ")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    anio_ingreso = int(input("Ingrese año de ingreso: "))