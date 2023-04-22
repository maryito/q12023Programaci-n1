# Guardar
# ACTUALIZAR LA RUTA
from pathlib import Path

# Librería para obtener ubicación de mi directorio
path = Path.cwd()

# dir = "/Users/maryito/clase/Clase PG1/Proyecto/data/"
dir =  str(path) + "/Proyecto/data/"
filename = dir + "users.txt"

def guardarArchivo(info):
    borrarEspacio = info.strip()
    tam = len(borrarEspacio)
    if tam > 0:
        f = open(filename, "a+")
        # temp =  "\n" + info
        temp =  "\n" + info
        f.writelines(temp)
        f.close()
    else:
        print("No se puede almacenar información vacía")

nom =  input("Usuario: ")
passwd =  input("Password: ")
save = nom + "," + passwd
guardarArchivo(save)

def leerArchivo(filename):
    lista_temp = []
    # Leer
    with open(filename, "r+") as f:
        for item in f.readlines():
            info =  item.split(',')

            # Posicion 0 - usuario
            # Posicion 1 - password
            _nombre = info[0]
            _password = info[1]

            # almacenando en lista
            lista_temp.append([_nombre, _password])
    f.close()
    return lista_temp

def listadoUser():
    lista_temp = []
    # Leer
    with open(filename, "r+") as f:
        for item in f.readlines():
            borrarEspacio = item.strip()
            tam = len(borrarEspacio) 
            if tam > 0:
                info =  item.split(',')

                # Posicion 0 - usuario
                # Posicion 1 - password
                _nombre = info[0]
                tmp = info[1].split("\n")
                _password = tmp[0]

                # almacenando en lista
                lista_temp.append([_nombre, _password])
    f.close()
    return lista_temp
# ejemplos
# temp = leerArchivo(filename)
# print(temp)