
def sumar_numeros_archivo(archivo_a, archivo_b):#Definimos la funcion

        with open(archivo_a, 'r') as entrada: #Abrimos el Archivo
            suma = sum(int(numero) for linea in entrada for numero in linea.strip().split(',')) #Recorremos el archivo y sumamos los numeros
            print(f"La suma de los numeros encontrados en el archivo es igual a {suma}") #imprimimos el resultado de la suma y agregamos un separador en la consola
            print("__________________________________________________________________")

        with open(archivo_b, 'w') as salida: 
            salida.write(str(suma)) #Escribimos el archivo con los resultados, si no existe se crea un archivo con los resultados
            print(f"Resultados guardados en {archivo_b}")

#Definimos los dos archivos
archivo_entrada = 'D:\\Escritorio\\Uni 2024\\Lab2\\Practicos\\Practico3\\numeros.csv'
archivo_salida = 'D:\\Escritorio\\Uni 2024\\Lab2\\Practicos\\Practico3\\resultado.txt'

# Llamamos a la funcion
sumar_numeros_archivo(archivo_entrada,archivo_salida )

