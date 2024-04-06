def sumar_numeros_archivo(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as f:
        numeros = [int(linea.strip()) for linea in f.readlines()] # Leer números del archivo
        suma = sum(numeros) # Calcular la suma
with open(archivo_salida, 'w') as f:
    f.write(str(suma)) # Escribir la suma en el archivo de salida
# Llamada a la función
sumar_numeros_archivo('numeros.txt', 'resultado.txt')