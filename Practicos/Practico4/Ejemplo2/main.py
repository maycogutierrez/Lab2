class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    def get_edad(self):
        return self._edad
    def set_edad(self, nueva_edad):
        self._edad = nueva_edad
