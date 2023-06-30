import mysql.connector

class Conectar_Base_de_Datos():

    def __init__(self) -> None:
        try:
            conexion = mysql.connector(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'Willyrex32/',
                db = 'db_negocio_panaderia',
            )
            if self.conexion.is_connected():
                print("Se a conectado con la base de datos")   
        except:
             print("No se pudo conectar con la base de datos")
        finally: 
            if self.conexion.is_connected():
                self.conexion.close()
                print("LA CONEXION FUE CERRADA")

           
  





        







