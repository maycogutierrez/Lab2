archivo = open("D:\\Escritorio\\Uni 2024\\Lab2\\Clase1\\Ejercicio1\\juegos.txt", "r")
lineas = archivo.readlines()

for linea in lineas:
    datos = linea.strip().split(',')
    print(f"Juego: {datos[0]} con Calificación {datos[1]} y Precio {datos[2]}")