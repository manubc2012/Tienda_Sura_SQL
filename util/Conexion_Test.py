

from util.Conexion import Conexion

def test_conexion_db():
    try:
        # Obtener la instancia de Conexion
        conexion = Conexion.get_instance()

        # Ejecutar una consulta simple
        resultado = conexion.execute_query("SELECT 1")

        # Verificar el resultado
        if resultado and resultado[0][0] == 1:
            print("Prueba de conexión a la base de datos exitosa.")
        else:
            print("La prueba de conexión a la base de datos falló.")
    except Exception as e:
        print(f"Error durante la prueba de conexión a la base de datos: {e}")

# Ejecutar la prueba
test_conexion_db()