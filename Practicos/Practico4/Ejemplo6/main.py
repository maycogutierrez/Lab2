import pdb
class Calculadora:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sumar(self):
        resultado = self.x + self.y
        return resultado
# Creación de objeto
calc = Calculadora(5, 3)
# Uso de pdb para debugging
pdb.set_trace()
resultado = calc.sumar()
print("El resultado es:", resultado)