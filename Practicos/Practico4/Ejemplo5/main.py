


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."
    
    def __str__(self):
        return f"Persona: {self.nombre}, Edad: {self.edad}"

# Creación de objeto y uso de métodos
persona1 = Persona("Juan", 30)
print(persona1.saludar())  # Salida: Hola, soy Juan y tengo 30 años.
print(persona1)             # Salida: Persona: Juan, Edad: 30

# Uso de métodos de acceso
persona1.nombre = "Carlos"
print(persona1.nombre)      # Salida: Carlos
print(persona1)             # Salida: Persona: Carlos, Edad: 30
