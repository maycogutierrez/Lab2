archivo = open("D:\\Escritorio\\Uni 2024\\Lab2\\Clase1\\Ejercicio2\\datos.txt", "r")
lineas = archivo.readlines()

data = []

for line in lineas:
    datos = line.strip().split(';')
    media = (int(datos[1]) + int(datos[2]) + int(datos[3]) + int(datos[4])) / 4
    print(f"Año: {datos[0]} Media facturación: {media}")
    data.append((int(datos[0]), media))

archivo.close()
data.sort()

guardar= input("Desea Guardar estos datos? Si/No ")

if guardar.lower() == "si":
    print("Datos Guardados Correctamente")
    archivo_ordenado = open("D:\\Escritorio\\Uni 2024\\Lab2\\Clase1\\Ejercicio2\\datos_ordenados.txt", "w")

    for año, media in data:
        archivo_ordenado.write(f"Ano:{año},Media:{media}\n")
    
    archivo_ordenado.close()  
else:
    print("Gracias por usar nuestro servicio, Adios!")


