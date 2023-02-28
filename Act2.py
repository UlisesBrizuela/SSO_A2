import os
import shutil
import random

for ruta, directorios, archivos in os.walk('D:/Drive/SISTEMAS OPERATIVOS/Seminario Sistemas Operativos/Act2/carpeta'):
    for archivo in archivos:
        ruta_archivo = os.path.join(ruta, archivo)
        ruta_copia = ruta_archivo + '_copia'
        shutil.copy(ruta_archivo, ruta_copia)

        with open(ruta_copia, 'r+') as Archivo:
            nuevo_texto = ""
            for linea in Archivo:
                for palabra in linea.split(" "):
                    for caracter in palabra:
                        if caracter.isdigit():
                            caracter = chr(random.randint(65, 90))
                        elif caracter.isalpha():
                            caracter = str(random.randint(0, 9))
                        nuevo_texto = nuevo_texto + str(caracter)
                    if nuevo_texto.endswith("\n"):
                        pass
                    else:
                        nuevo_texto = nuevo_texto + " "

            Archivo.seek(0)
            Archivo.write(nuevo_texto)
            Archivo.truncate()