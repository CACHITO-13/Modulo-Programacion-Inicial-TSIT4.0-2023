import mysql.connector

class Conectar_Base_de_Datos():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.conect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '********',
                db = 'db_negocio_panaderia',
            )
        except mysql.connector.Error as descripcionError:
            print("No se puedo conectar a la base de datos",descripcionError)
def Insertar_Producto(self,PRODUCTOS):
    if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sentenciaSQL = "INSERT INTO PRODUCTOS values(null,%s,%s)"
            data = (PRODUCTOS.getId_Producto(),
                    PRODUCTOS.getPrecio(),
                    PRODUCTOS.getProveedor(),
                    )
            
            cursor.execute(sentenciaSQL,data)
            cursor.Conexion.commit()
            cursor.Conexion.close()   
            print("Producto insertado correctamente")

        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conctar la Base de Datos", descripcionDelError)

    
def Listado_De_Productos(self):
    if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sentenciaSQL = "SELECT * FROM PRODUCTOS"
            cursor.execute(sentenciaSQL)
            resultados= cursor.fetchall()
            cursor.Conexion.close()
            return resultados
            
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conctar la Base de Datos", descripcionDelError)  


        







