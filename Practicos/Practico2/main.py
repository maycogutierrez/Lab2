#Ejercicio:
#Escribe un programa en Python que lea el archivo datos.txt, calcule el promedio de las edades y luego escriba el nombre de cada persona #junto con un mensaje que indique si son mayores o menores que el promedio de edad en otro archivo llamado resultado.txt.

archivo = open("D:\\Escritorio\\Uni 2024\\Lab2\\Practicos\\Practico2\\datos.txt", "r")
lineas = archivo.readlines()

dataEdad = []
data = []

for line in lineas:
    datos = line.strip().split(" ")
    dataEdad.append((int(datos[1])))
    data.append((datos[0], (int(datos[1]))))

archivo.close()
media = sum(dataEdad) / len(dataEdad)
archivo_resultado = open("D:\\Escritorio\\Uni 2024\\Lab2\\Practicos\\Practico2\\resultado.txt", "w")

for nombre, edad in data:
    if edad > media:
        mensaje = f"{nombre} es mayor que el promedio de edad."
        print(mensaje)
    elif edad < media:
        mensaje = f"{nombre} es menor que el promedio de edad."
        print(mensaje)
    else:
        mensaje = f"{nombre} tiene la misma edad que el promedio de edad."
        print(mensaje)
    archivo_resultado.write(mensaje + '\n')


archivo_resultado.close()

print("Proceso completado. Revisa el archivo de resultado para ver el resultado.")