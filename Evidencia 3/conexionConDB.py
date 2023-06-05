import mysql.connector


class Conectar_Base_De_Datos():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '2534inti',
                db = 'prueba'
            )
        except mysql.connector.Error as descripcionError:
            print("No se pudo conectar la base de datos", descripcionError)
