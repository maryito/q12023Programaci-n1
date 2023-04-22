def menuPrincipal():
    listaOpciones = ["modulo1", "modulo2", "modulo3"]
    print("\t Pantalla de Home del sistema")
    contado = 0
    for itemOpc in listaOpciones:
        contado =  contado + 1
        print(str(contado), " - ", itemOpc)
    opc = int(input("Seleccione una opción ==> "))
    if opc <= len(listaOpciones):
        return opc
    else:
        print("Opción invalidad ")

#Ejemplo
# men = menuPrincipal()
# print("Opción selecciona es = ", men)