
import mysql.connector
from mysql.connector import Error

class Conexion:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Conexion, cls).__new__(cls)
            try:
                cls._instance.conexion = mysql.connector.connect(
                    host='localhost',
                    port = 3306,
                    user='root',
                    password='password123',
                    database='tienda_sura'

                )
                cls._instance.cursor = cls._instance.conexion.cursor()
                print("Conexión a MySQL establecida")
            except Error as e:
                print(f"Error al conectar a MySQL: {e}")
        return cls._instance

    @staticmethod
    def get_instance():
        if Conexion._instance is None:
            Conexion()
        return Conexion._instance

    def execute_query(self, consulta):
        try:
            self.cursor.execute(consulta)
            resultados = self.cursor.fetchall()
            return resultados
        except Error as e:
            print(f"Error al ejecutar consulta: {e}")

    def disconnect(self):
        if self.conexion.is_connected():
            self.cursor.close()
            self.conexion.close()
            print("Conexión a MySQL cerrada")