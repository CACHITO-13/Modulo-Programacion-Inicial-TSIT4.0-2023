import Controlador

while True:
    print("\n+-------------------------------------------+")
    print("|         Big Bread SA         |")
    print("+-------------------------------------------+\n")
    print("")
    print("MENÚ PRINCIPAL\n")
    print("1 - INGRESAR PRODUCTO")
    print("2 - ACTUALIZAR PRODUCTO")
    print("3 - ELIMINAR PRODUCTO")
    print("8 - SALIR")
    print("\n")
    opcion = int(input("Ingrese su opción: "))
    if opcion == 1:
        Controlador.Insertar_Producto()
    elif opcion == 2:
        Controlador.Actualizar_Producto()
    elif opcion == 3:
        Controlador.Eliminar_Producto()
    elif opcion == 4:
        None
    elif opcion == 5:
        Controlador.Listar_Productos()
    elif opcion == 6:
        None
    elif opcion == 7:
        None
    elif opcion == 8:
        break
    else:
        print("¡Opción incorrecta!")