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
            return self.sueldo_basico
        elif 2 <= anios <= 5:
            return self.sueldo_basico * 1.05
        else:
            return self.sueldo_basico * 1.10

class EmpleadoComision(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, salario_minimo, clientes_captados, monto_por_cliente):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente

    def salario(self):
        return max(self.salario_minimo, self.clientes_captados * self.monto_por_cliente)

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
    categoria = Categoria(int(input("Ingrese categoría (1 para FIJO, 2 para COMISION): ")))

    if categoria == Categoria.FIJO:
        sueldo_basico = float(input("Ingrese sueldo básico: "))
        return EmpleadoFijo(dni, nombre, apellido, anio_ingreso, sueldo_basico)
    else:
        salario_minimo = float(input("Ingrese salario mínimo: "))
        clientes_captados = int(input("Ingrese número de clientes captados: "))
        monto_por_cliente = float(input("Ingrese monto por cliente: "))
        return EmpleadoComision(dni, nombre, apellido, anio_ingreso, salario_minimo, clientes_captados, monto_por_cliente)

def main():
    empleados = []
    while True:
        empleados.append(ingresar_datos_empleado())
        mas_empleados = input("¿Desea ingresar más empleados? (s/n): ")
        if mas_empleados.lower() != 's':
            break

    mostrarSalarios(empleados)
    empleado_mas_clientes = empleadoConMasClientes(empleados)
    print(f'El empleado con más clientes es: {empleado_mas_clientes[0]} {empleado_mas_clientes[1]}')

if __name__ == "__main__":
    main()
