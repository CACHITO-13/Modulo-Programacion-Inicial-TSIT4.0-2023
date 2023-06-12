class Producto():
    Id_producto = 0,
    Precio = 0,
    Proveedor = "",

def __init__(self,id_producto,precio,proveedor):
    self.Id_producto = id_producto
    self.Precio = precio
    self.Proveedor = proveedor

    def getid_producto(self):
        return id_producto
    def getprecio(self):
        return precio
    def getproveedor(self):
        return proveedor
    
    def setid_producto(self,id_producto):
        self.id_prodcuto = id_producto
    
    def setprecio(self,precio):
        set.precio = precio
    
    def setproveedor(self,proveedor):
        set.proveedor = proveedor

class Insumo():
    Id_insumo = 0,
    Nombre_insumo = "",

def __init__(self,id_insumo,nombre_insumo):
    self.Id_insumo = id_insumo
    self.Nombre_insumo = nombre_insumo

    def getid_insumo(self):
        return id_insumo
    def getnombre_insumo(self):
        return nombre_insumo
    
    def setid_insumo(self,id_insumo):
        self.id_insumo
    def setnombre_insumo(self,nombre_insumo):
        self.nombre_insumo

class Compras():
    Id_compra = 0,
    Proveedor = "",
    Id_pedido = 0,

def __init__(self,id_compra,proveedor,id_pedido):
    self.Id_compra = id_compra
    self.Proveedor = proveedor
    self.Id_pedido = id_pedido


    def getid_pedido(self):
        return id_pedido
    def getproveedor(self):
        return proveedor
    def getid_compra(self):
        return id_compra
        
    def setid_pedido(self,id_pedido):
        self.id_pedido = id_pedido
    def setproveedor(self,proveedor):
        self.proveedor = proveedor
    def setid_compra(self,id_compra):
        self.id_compra = id_compra

class Pedido():
    Id_pedido = 0,
    Id_empleado = 0,
    Id_producto = 0,
    Total = 0,

def __init__(self,id_pedido,id_empleado,id_producto,total):
    self.Id_pedido = id_pedido
    self.Id_empleado = id_empleado
    self.Id_producto = id_producto
    self.Total = total

    def getid_pedido(self):
        return id_pedido
    def getid_empleado(self):
        return id_empleado
    def getid_producto(self):
        return id_producto
    def gettotal(self):
        return total
    
    def setid_pedido(self,id_pedido):
        self.id_pedido = id_pedido
    def setid_producto(self,id_producto):
        self.id_producto = id_producto
    def setid_empleado(self,id_empleado):
        self.id_empleado = id_empleado
    def settotal(self,total):
        self.total = total
        
class Empleados():
    Id_empleado = 0,
    DNI = 0,
    Nombre = "",

def __init__(self,id_empleado,dNI,nombre):
    self.Id_empleado = id_empleado
    self.DNI = dNI
    self.Nombre = nombre

    def getid_empleado(self):
        return id_empleado
    def getdNI(self):
        return dNI
    def getnombre(self):
        return nombre
    

    def setid_empleado(self,id_empleado):
        self.id_empleado = id_empleado
    def setdNI(self,id_dNI):
        self.dNI = dNI
    def setnombre(self,nombre):
        self.nombre = nombre

class Produccion_Diaria():
    Id_produccion = 0,
    Fecha_produccion = "",
    Id_producto = 0,
    Cantidad_Producida = 0,

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
        