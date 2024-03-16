class Vendedor:
    categoria_salario = {
        'A': {'salario_base': 7000, 'premio_por_vehiculo': 700},
        'B': {'salario_base': 8200, 'premio_por_vehiculo': 600},
        'C': {'salario_base': 12500, 'premio_por_vehiculo': 500}
    }

    def __init__(self, nombre, antiguedad, categoria, vehiculos_vendidos):
        self.nombre = nombre
        self.antiguedad = antiguedad
        self.categoria = categoria
        self.salario_base = self.categoria_salario[categoria]['salario_base']
        self.premio_por_vehiculo = self.categoria_salario[categoria]['premio_por_vehiculo']
        self.vehiculos_vendidos = vehiculos_vendidos

    def calcular_sueldo_total(self):
        return self.salario_base + (self.premio_por_vehiculo * self.vehiculos_vendidos)

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

# Inscripción de vendedores y clientes
vendedores = []
clientes = []

# Inscripción de 3 vendedores
for i in range(3):
    nombre = input(f"\nIngrese el nombre del vendedor {i+1}: ")
    antiguedad = int(input(f"Ingrese la antigüedad de {nombre} en años: "))
    categoria = input(f"Ingrese la categoría de {nombre}:\nA para Principiante\nB para Nivel medio\nC para Experto\n").upper()
    vehiculos_vendidos = int(input(f"Ingrese la cantidad de vehículos vendidos por {nombre}: "))
    vendedor = Vendedor(nombre, antiguedad, categoria, vehiculos_vendidos)
    vendedores.append(vendedor)

# Inscripción de 3 clientes
for i in range(3):
    nombre = input(f"\nIngrese el nombre del cliente {i+1}: ")
    cliente = Cliente(nombre)
    clientes.append(cliente)

# Visualización de sueldos totales de vendedores
print("\nSueldo Total de Vendedores:")
for vendedor in vendedores:
    print(f"{vendedor.nombre} - Sueldo Total: {vendedor.calcular_sueldo_total()} - Antiguedad: {vendedor.antiguedad}")

# Listado de todos los clientes
print("\nLista de Clientes:")
for cliente in clientes:
    print(f"{cliente.nombre}")