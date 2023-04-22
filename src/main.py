

from utility.menu import menuPrincipal
from login import login, singUp
#from src.utility.menu import menuPrincipal

if __name__ == '__main__':
    while True:
        salir = ""
        # LOGIN
        val = login()

        if val == False:
            opcRegistrarte = input("¿Desea regístrate Si - No ?").upper()
            if opcRegistrarte == "SI":
                # REGISTRO
                singUp()
        while val:
            print("Menu Principal")
            # invoco a mi menu
            menuPrincipal()
            
            #Función para esperar
            input()
            opcContinuar = input("¿Desea continuar Si o No ?").upper()
            if opcContinuar == "NO":
                val = False
    
        salir = input("¿Desea Salir Si o No ?").upper()
        if salir == "SI":
            break

