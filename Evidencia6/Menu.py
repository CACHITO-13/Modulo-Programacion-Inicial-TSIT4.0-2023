import _mysql_connector
import tablas
def ListarProductos():
    con = tablas.Conectar()
    listado = con.Listar_Productos()
    print("\n| ID PRODUCTO   |   NOMBRE PRODUCTO    |    PRECIO     ")
    for producto in listado:
        print(' ',producto[0],"\t\t",producto[1],"\t\t",str(producto[2]))
    input("Para continuar presione enter")

def Insertar_Producto():
    con = tablas.Conectar()
    id_producto = input("\nIngrese el nombre del Producto: ")
    nombre = input("\nIngrese el nombre del Producto: ")
    precio= int(input("\nIngrese el precio del Producto: "))
    
    nuevoProducto = tablas.Producto(0,id_producto,nombre,precio,0)

    con.InsertarProducto(nuevoProducto)
    input("Para continuar presione enter")


def Actualizar_Producto():
    con = tablas.conectar()
    id_producto = input("\nIngrese el nuevo nombre del Producto: ")
    nombre = input("\nIngrese el nuevo nombre del producto: ")
    precio = int(input("\nIngrese el nuevo precio del producto: "))

    productoActualizado = tablas.Producto(0,id_producto,nombre,precio,0)
    con.ActualizarProducto(productoActualizado)
    input("Para continuar presione enter")

def Eliminar_Producto():
    con = tablas.conectar()
    id_producto = input("\n Ingrese el id del producto que desea eliminar: ")
    producto_eliminado = tablas.Producto(0,id_producto,0)
    con.EliminarProducto(producto_eliminado)
    input("Presione enter para continuar")


def Insertar_Insumo():
    con = tablas.Conectar()
    id_insumo = input("\nIngrese el id del Insumo: ")
    nombre_insumo = input("\nIngrese el nombre del Insumo: ")
    unidad_medida= input("\nIngrese la unidad de medida: ")
    cantidad = int(input("\nIngrese la cantidad del insumo"))
    nuevoInsumo = tablas.Insumo(0,id_insumo,nombre_insumo,unidad_medida,cantidad,0)
    con.InsertarInsumo(nuevoInsumo)
    input("Para continuar presione enter")


def Actualizar_Insumo():
    con = tablas.conectar()
    id_insumo = input("\nIngrese el nuevo nombre del Insumo: ")
    nombre_insumo = input("\nIngrese el nuevo nombre del Insumo: ")
    cantidad = input("\nIngrese la cantidad del insumo: ")
    unidad_medida = int(input("Ingrese la unidad de medida: "))
    insumo_Actualizado = tablas.Insumo(0,id_insumo,nombre_insumo,cantidad,unidad_medida,0)
    con.Actualizar_Insumo(insumo_Actualizado)
    input("Para continuar presione enter")

def Eliminar_Insumo():
    con = tablas.conectar()
    id_insumo = input("\n Ingrese el id del insumo que desea eliminar: ")
    insumo_eliminado = tablas.Insumo(0,id_insumo,0)
    con.EliminarInsumo(insumo_eliminado)
    input("Presione enter para continuar")

def Insertar_Produccion_diaria():
    con = tablas.Conectar()
    id_produccion = input("\nIngrese el id de la produccion: ")
    fecha_produccion = input("\nIngrese la fecha de produccion: ")
    id_producto = input("\nIngrese el id del Producto producido: ")
    cantidad_producida = int(input("\nIngrese la cantidad producida de ese dia: "))
    nueva_produccion = tablas.Produccion_diaria(0,id_produccion,fecha_produccion,id_producto,cantidad_producida,0)

    con.Insertar_Produccion_diaria(nueva_produccion)
    input("Para continuar presione enter")

def Actualizar_Produccion_diaria():
    con = tablas.Conectar()
    id_produccion = input("\nIngrese el id de la produccion: ")
    fecha_produccion = input("\nIngrese la fecha de produccion: ")
    id_producto = input("\nIngrese el id del Producto producido: ")
    cantidad_producida = int(input("\nIngrese la cantidad producida de ese dia: "))
    produccion_Actualizada = tablas.Produccion_diaria(0,id_produccion,fecha_produccion,id_producto,cantidad_producida,0)
    con.Actualizar_Produccion_diaria(produccion_Actualizada)
    input("Para continuar presione enter")

def Eliminar_Produccion_diaria():
    con = tablas.conectar()
    id_produccion = input("\n Ingrese el id del producto que desea eliminar: ")
    produccion_eliminada = tablas.Produccion_diaria(0,id_produccion,0)
    con.Eliminar_Produccion_diaria(produccion_eliminada)
    input("Presione enter para continuar")


def Insertar_Receta():
    con = tablas.Conectar()
    id_receta= input("\nIngrese el id de la nueva receta: ")
    id_producto = input("\nIngrese el id del Producto que va a crear: ")
    id_insumo= int(input("\nIngrese el id del insumo que va a utilizar: "))
    cantidad_usada = int(input("\nIngrese la cantidad necesaria para hacer la receta: "))
    nueva_Receta= tablas.Recetas(0,id_producto,id_insumo,id_receta,cantidad_usada,0)
    con.Insertar_Receta(nueva_Receta)
    input("Para continuar presione enter")


def Actualizar_Receta():
    con = tablas.Conectar()
    id_receta= input("\nIngrese el id de la receta que quiere actualizar: ")
    id_producto = input("\nIngrese el id del Producto que va a crear: ")
    id_insumo= int(input("\nIngrese el id del insumo que va a utilizar: "))
    cantidad_usada = int(input("\nIngrese la cantidad necesaria para hacer la receta: "))

    receta_Actualizada = tablas.Recetas(0,id_producto,id_receta,id_insumo,cantidad_usada,0)
    con.Actualizar_Receta(receta_Actualizada)
    input("Para continuar presione enter")

def Eliminar_Receta():
    con = tablas.conectar()
    id_receta= input("\nIngrese el id de la receta que desea eliminar: ")
    receta_Eliminada = tablas.Producto(0,id_receta,0)
    con.Eliminar_Receta(receta_Eliminada)
    input("Presione enter para continuar")

def obtener_produccion_total_rango():
    con = tablas.conectar()
    fecha_inicio = int(input("\nIngrese la fecha de inicio de la produccion: "))
    fecha_fin = int(input("\nIngrese la fecha del final de la produccion: "))
    produccion_rango = tablas.produccion_total(0,fecha_fin,fecha_inicio,0)
    con.obetener_produccion_total_rango(produccion_rango)
    input("Presione enter para continuar")


def insumo_por_dia():

    con = tablas.conectar()
    fecha = int(input("\n Ingrese la fecha de la que quiere "))



