archivo = open("D:\\Escritorio\\Uni 2024\\Lab2\\Clase1\\Ejercicio3\\datos.txt", "r")
    
lineas = archivo.readlines()

resultados = []

for linea in lineas:
    elementos = linea.strip().split(',')
    resultados.append([int(elemento) for elemento in elementos])


for equipo_fila in range(len(resultados)):
    puntos_equipo = 0
    for equipo_columna in range(len(resultados[equipo_fila])):
        goles_equipo_fila = resultados[equipo_fila][equipo_columna]
        goles_equipo_columna = resultados[equipo_columna][equipo_fila]
        
        if equipo_fila != equipo_columna:
            if goles_equipo_fila > goles_equipo_columna:
                print(f"Equipo {equipo_fila + 1} marcó {goles_equipo_fila} goles contra equipo {equipo_columna + 1}")
                puntos_equipo += 3
            elif goles_equipo_fila < goles_equipo_columna:
                print(f"Equipo {equipo_fila + 1} perdió {goles_equipo_fila} goles contra equipo {equipo_columna + 1}")
            else:
                print(f"Equipo {equipo_fila + 1} empató {goles_equipo_fila} goles contra equipo {equipo_columna + 1}")
                puntos_equipo += 1
    print(f"El equipo {equipo_fila + 1} suma {puntos_equipo} puntos")
    print("________________________________________________________")
