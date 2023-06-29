import Menu
while True:
    print("\n+-------------------------------------------+")
    print("|         Big Bread SA         |")
    print("+-------------------------------------------+\n")
    print("")
    print("MENÚ PRINCIPAL\n")
    print("1 - INGRESAR / ELIMINAR / MODIFICACION DE PRODUCTO")
    print("2 - INGRESAR / ELIMINAR / MODIFICACION DE INSUMO")
    print("3 - INGRESAR / ELIMINAR / MODIFICACION DE PRODUCCION DIARIA")
    print("4 - INGRESAR / ELIMINAR / MODIFICACION DE RECETAS")
    print("5 - LISTAR TODA LA PRODUCCION DE UN DIA PUNTUAL")
    print("6 - LISTADO DE INSUMOS DIARIO UTILIZADOS")
    print("8 - SALIR")
    print("\n")
    opcion = int(input("Ingrese su opción: "))
    if opcion == 1:
        segunda_opcion = int(input("INDIQUE ESPECIFICAMENTE LO QUE QUIERE HACER: "))
        print("1- INGRESAR UN PRODUCTO")
        print("2- ACTUALIZAR UN PRODUCTO")
        print("3- ELIMINAR UN PRODUCTO")
        if segunda_opcion == 1:
            Menu.InsertarProducto()
        elif segunda_opcion == 2:
            Menu.ActualizarProducto()
        else: segunda_opcion == 3
        Menu.Eliminar_Producto()
    
    elif opcion == 2:
        segunda_opcion = int(input("INDIQUE ESPECIFICAMENTE LO QUE QUIERE HACER: "))
        print("1- INGREAR UN INSUMO")
        print("2- ACTUALIZAR UN INSUMO")
        print("3- ELIMINAR UN INSUMO")
        if segunda_opcion == 1:
            Menu.Insertar_Insumo()
        elif segunda_opcion == 2:
            Menu.Actualizar_Insumo()
        else: segunda_opcion == 3
        Menu.Eliminar_Insumo()
    
    elif opcion == 3:
        segunda_opcion = int(input("INDIQUE ESPECIFICAMENTE LO QUE QUIERE HACER: "))
        print("1- INGRESAR LA PRODUCCION DIARIA")
        print("2- ACTUALIZA LA PRODUCCION DIARIA")
        print("3- ELIMINAR LA PRODUCCION DIARIA")
        if segunda_opcion == 1:
            Menu.Insertar_Produccion_Diaria()
        elif segunda_opcion == 2:
            Menu.Actualizar_Produccion_Diaria()
        else: segunda_opcion == 3
        Menu.Eliminar_Produccion_diaria()
    
    elif opcion == 4:
    
        segunda_opcion = int(input("INDIQUE ESPECIFICAMENTE LO QUE QUIERE HACER: "))
        print(1- "INGRESAR UNA NUEVA RECETA")
        print(2- "ACTULIZA UNA RECETA")
        print(3- "ELIMINA UNA RECETA")
        if segunda_opcion == 1:
            Menu.Insertar_Receta()
        elif segunda_opcion == 2:
            Menu.Actualizar_Receta()
        else: segunda_opcion == 3
        Menu.Eliminar_Receta()
    
    elif opcion == 5:
        Menu.obtener_produccion_diaria
    
    elif opcion == 6:
        
        Menu.obtener_produccion_rango

    elif opcion == 7:



    
        Menu.insumos_por_dia
    
    
    else:
        print("¡Opción incorrecta!")