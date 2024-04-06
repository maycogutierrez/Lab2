# Función con parámetros posicionales
def suma(a, b):
    return a + b
# Función con parámetros por nombre (keyword)
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"
# Función con parámetro por nombre y posicionales
def division(dividendo, divisor, mensaje="El resultado es"):
    return f"{mensaje}: {dividendo // divisor}"
# Llamadas a las funciones
print(suma(5, 3)) # Output: 8
print(saludar("Juan")) # Output: Hola, Juan!
print(division(10, 2)) # Output: El resultado es: 5