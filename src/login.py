from src.archivo import listadoUser, guardarArchivo


def singUp():
    print("\t\tSING UP")
    user =  input("Ingrese su Usuario: ")
    password =  input("Ingrese su Password: ")
    info =  user + "," + password
    guardarArchivo(info)

# Ejemplo
# nom =  input("Usuario: ")
# passwd =  input("Password: ")

# singUp(nom, passwd)

def login():
    print("\t\tLOGIN")
    _nom =  input("Ingrese su Usuario: ")
    _passwd =  input("Ingrese su Password: ")
    status = False
    for user in listadoUser():
        _nombre = user[0]
        _password = user[1]

        if (_nom == user[0]) and (_passwd == user[1]):
            print("Usuarios Autenticado\n")
            status = True
            break
    if status == False:
        print("!Autenticación Fallida!\n")
    return status
