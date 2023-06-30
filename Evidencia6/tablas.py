import mysql.connector
from mysql.connector import conexion

class Producto():
    Id_producto = 0,
    Precio = 0,
    Nombre = "",

def __init__(self,id_producto,precio,nombre):
    self.Id_producto = id_producto
    self.Precio = precio
    self.Nombre = nombre

    def getid_producto(self):
        return id_producto
    def getprecio(self):
        return precio
    def getnombre(self):
        return nombre
    
    def setid_producto(self,id_producto):
        self.id_prodcuto = id_producto
    
    def setprecio(self,precio):
        set.precio = precio
    
    def sernombre(self,nombre):
        set.nombre = nombre

def Insertar_Producto(self,Producto):
    if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sentenciaSQL = "INSERT into productos values(%s,%s,%s)"
            datos = (Producto.getid_producto(),
                     Producto.getprecio(),
                    Producto.getgetnombre()
            )
            cursor.execute(sentenciaSQL, datos)
            self.conexion.commit()
            self.conexion.close()
            cursor.close()
            print("Producto insertado correctamente")
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar la Base de Datos:", descripcionDelError)

def Listar_Productos(self):
        conection = conexion.is_connected()
        try:
            cursor = self.conexion.cursor()
            sentenciaSQL = "SELECT * FROM productos"
            cursor.execute(sentenciaSQL)
            resultados= cursor.fetchall()
            cursor.Conexion.close()
            return resultados
            
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conctar la Base de Datos", descripcionDelError)

def Actualizar_Producto(self, id_producto, precio, nombre):
    if self.conexion.is_connected():
        Conectar_Base_de_Datos = conexion.Conectar()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "UPDATE productos SET precio=%s, nombre=%s WHERE id_producto=%s"
            datos = (precio, nombre, id_producto)
            cursor.execute(sentenciaSQL, datos)
            cursor.Conexion.commit()
            cursor.Conexion.close()   
            print("Producto actualizado correctamente")
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar la Base de Datos:", descripcionDelError)

def Eliminar_Producto(self, id_producto):
    if self.conexion.is_connected():
        Conectar_Base_de_Datos = conexion.Conectar()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "DELETE FROM productos WHERE id_producto=%s"
            datos = (id_producto,)
            cursor.execute(sentenciaSQL, datos)
            cursor.Conexion.commit()
            cursor.Conexion.close()   
            print("Producto eliminado correctamente")
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar la Base de Datos:", descripcionDelError)

"----------------------------------------------------------------------------------"
class Insumo():
    Id_insumo = 0,
    Nombre_insumo = "",
    Unidad_Medida = "",
    Cantidad = 0,

def __init__(self,id_insumo,nombre_insumo,unidad_medida,cantidad):
    self.Id_insumo = id_insumo
    self.Nombre_insumo = nombre_insumo
    self.Unidad_Medida = unidad_medida
    self.Cantidad = cantidad
    def getunidad_medida(self):
        return unidad_medida
    def getid_insumo(self):
        return id_insumo
    def getnombre_insumo(self):
        return nombre_insumo
    def getcantidad(self):
        return cantidad    
    def setunidad_medida(self,cantidad):
        self.cantidad_medida
    def setcantidad(self,cantidad):
        self.cantidad
    def setid_insumo(self,id_insumo):
        self.id_insumo
    def setnombre_insumo(self,nombre_insumo):
        self.nombre_insumo

def Insertar_Insumo (self,Insumo):

    if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sentenciaSQL = "Insert into insumos values(%s,%s,%s,%s)"
            datos = (Insumo.getid_insumo(),
                     Insumo.getnombre_insumo(),
                     Insumo.getcantidad(),
                     Insumo.getunidad_medida())
            cursor.execute(sentenciaSQL, datos)
            self.conexion.commit()
            self.conexion.close()
            cursor.close()
            print("Insumo insertado correctamente")
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar la Base de Datos:", descripcionDelError)
def Listar_Insumos(self):
        conection = conexion.is_connected()
        try:
            cursor = self.conexion.cursor()
            sentenciaSQL = "SELECT * FROM insumos"
            cursor.execute(sentenciaSQL)
            resultados= cursor.fetchall()
            cursor.Conexion.close()
            return resultados
            
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conctar la Base de Datos", descripcionDelError)

def Actualizar_Producto(self,id_insumo,nombre_insumo,unidad_medida,cantidad):
    if self.conexion.is_connected():
        Conectar_Base_de_Datos = conexion.Conectar()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "UPDATE insumos SET id_insumo = %s, nombre_insumo = %s, unidad_medida = %s, cantidad = %s"
            datos = (id_insumo,nombre_insumo,unidad_medida,cantidad)
            cursor.execute(sentenciaSQL, datos)
            cursor.Conexion.commit()
            cursor.Conexion.close()   
            print("Producto actualizado correctamente")
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar la Base de Datos:", descripcionDelError)

def Eliminar_Producto(self, id_insumo):
    if self.conexion.is_connected():
        Conectar_Base_de_Datos = conexion.Conectar()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "DELETE FROM insumos WHERE id_insumo=%s"
            datos = (id_insumo)
            cursor.execute(sentenciaSQL, datos)
            cursor.Conexion.commit()
            cursor.Conexion.close()   
            print("Producto eliminado correctamente")
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar la Base de Datos:", descripcionDelError)

"-------------------------------------------------------------------------------"
class Compras():
    Id_compra = 0,
    Proveedor = "",
    Id_insumo = 0,
    Fecha_compra = "",
    Monto_total = 0,

def __init__(self,id_compra,proveedor,id_insumo,fecha_compra,monto_total):
    self.Id_compra = id_compra
    self.Proveedor = proveedor
    self.Id_insumo = id_insumo
    self.Fecha_compra = fecha_compra
    self.Monto_total = monto_total

    def getid_insumo(self):
        return id_insumo
    def getproveedor(self):
        return proveedor
    def getid_compra(self):
        return id_compra
    def getfecha_compra(self):
        return fecha_compra
    def getmonto_total(self):
        return monto_total
    def setfecha_compra(self,fecha_compra):
        self.fecha_compra = fecha_compra
    def setmonto_total(self,monto_total):
        self.monto_total = monto_total
    def setid_insumo(self,id_insumo):
        self.id_insumo = id_insumo
    def setproveedor(self,proveedor):
        self.proveedor = proveedor
    def setid_compra(self,id_compra):
        self.id_compra = id_compra
"--------------------------------------------------------------------------------"
class Pedido():
    Id_pedido = 0,
    Cliente = "",
    Id_producto = 0,
    Total = 0,
    Fecha = "",

def __init__(self,id_pedido,cliente,id_producto,total,fecha):
    self.Id_pedido = id_pedido
    self.Cliente = cliente
    self.Id_producto = id_producto
    self.Total = total
    self.Fecha = fecha

    def getid_pedido(self):
        return id_pedido
    def getcliente(self):
        return cliente
    def getid_producto(self):
        return id_producto
    def gettotal(self):
        return total
    def getfecha(self):
        return fecha
    
    def setfecha(self,fecha):
        self.fecha = fecha
    
    def setid_pedido(self,id_pedido):
        self.id_pedido = id_pedido
    def setid_producto(self,id_producto):
        self.id_producto = id_producto
    def setcliente(self,cliente):
        self.cliente = cliente
    def settotal(self,total):
        self.total = total
"-----------------------------------------------------------------------------------"        
class Empleados():
    Id_empleado = 0,
    DNI = 0,
    Nombre = "",
    Sueldo = 0,
    Puesto = "",
    Telefono = "",

def __init__(self,id_empleado,dNI,nombre,sueldo,puesto,telefono):
    self.Id_empleado = id_empleado
    self.DNI = dNI
    self.Nombre = nombre

    def getid_empleado(self):
        return id_empleado
    def getdNI(self):
        return dNI
    def getnombre(self):
        return nombre
    def getsueldo(self):
        return sueldo
    def getpuesto(self):
        return puesto
    def gettelefono(self):
        return telefono
    
    def setsueldo(self,sueldo):
        self.sueldo = sueldo 
    def setpuesto(self,puesto):
        self.puesto = puesto
    def settelefono(self,telefono):
        self.telefono = telefono


    def setid_empleado(self,id_empleado):
        self.id_empleado = id_empleado
    def setdNI(self,id_dNI):
        self.dNI = dNI
    def setnombre(self,nombre):
        self.nombre = nombre
"--------------------------------------------------------------------------------"
class Produccion_Diaria():
    Id_produccion = 0,
    Fecha_produccion = "",
    Id_producto = 0,
    Cantidad_Producida = 0,

def Insertar_Produccion_diaria (self,Produccion_Diaria):

    if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sentenciaSQL = "Insert into insumos values(%s,%s,%s,%s)"
            datos = (Produccion_Diaria.getid_produccion(),
                     Produccion_Diaria.getfecha_produccion(),
                     Produccion_Diaria.getcantidad_producida(),
                     Produccion_Diaria.getid_producto())
            cursor.execute(sentenciaSQL, datos)
            self.conexion.commit()
            self.conexion.close()
            cursor.close()
            print("Produccion diaria insertada correctamente")
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar la Base de Datos:", descripcionDelError)

def Actualizar_Produccion_diaria(self, id_produccion, fecha_produccion, id_producto, cantidad_producida):

    if self.conexion.is_connected():
        Conectar_Base_de_Datos = conexion.Conectar()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "UPDATE produccion_diaria SET id_produccion = %s, fecha_produccion = %s, id_producto = %s, cantidad_producida = %s"
            datos = (id_produccion, fecha_produccion, id_producto, cantidad_producida)
            cursor.execute(sentenciaSQL, datos)
            cursor.Conexion.commit()
            cursor.Conexion.close()   
            print("Producto actualizado correctamente")
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar la Base de Datos:", descripcionDelError)

def Eliminar_Produccion_diaria(self, id_produccion):
    if self.conexion.is_connected():
        Conectar_Base_de_Datos = conexion.Conectar()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "DELETE FROM productos WHERE id_produccion=%s"
            datos = (id_produccion)
            cursor.execute(sentenciaSQL, datos)
            cursor.Conexion.commit()
            cursor.Conexion.close()   
            print("Produccion diaria eliminada correctamente")
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar la Base de Datos:", descripcionDelError)

def __init__(self,id_produccion,fecha_produccion,id_producto,cantidad_producida):
    self.Id_produccion = id_produccion
    self.Fecha_produccion = fecha_produccion
    self.Id_producto = id_producto
    self.Cantidad_producida = cantidad_producida

    def getid_produccion(self):
        return id_produccion
    def getfecha_produccion(self):
        return fecha_produccion
    def getid_producto(self):
        return id_producto
    def getcantidad_producida(self):
        return cantidad_producida
    
    def setid_produccion(self,id_produccion):
        self.id_produccion = id_produccion
    def setfecha_produccion(self,fecha_produccion):
        self.fecha_produccion = fecha_produccion
    def setid_producto(self,id_producto):
        self.id_producto = id_producto
    def setcantidad_producida(self,cantidad_producida):
        self.cantidad_producida = cantidad_producida
"----------------------------------------------------------------------------------"
class Recetas():
    Id_receta = 0,
    Id_producto = 0,
    Id_insumo = 0,
    Cantidad_usada = 0,

def __init__(self,id_receta,id_producto,id_insumo,cantidad_usada):
    self.Id_receta = id_receta
    self.Id_producto = id_producto
    self.Id_insumo = id_insumo
    self.Cantidad_usada = cantidad_usada


    def getid_receta(self):
        return id_receta
    def getid_producto(self):
        return id_producto
    def getid_insumo(self):
        return id_insumo
    def getcantidad_usada(self):
        return cantidad_usada
    
    def setid_receta(self,id_receta):
        self.id_receta = id_receta
    def setid_producto(self,id_producto):
        self.id_producto = id_producto
    def setid_insumo(self,id_insumo):
        self.id_insumo = id_insumo
    def setcantidad_usada(self,cantidad_usada):
        self.cantidad_usada = cantidad_usada
"---------------------------------------------------------------------------------------"        