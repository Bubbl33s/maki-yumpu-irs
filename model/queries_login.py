import pyodbc
from model.db_conn import Database


class LoginQuery:
    def __init__(self):
        self.db = Database()
    
    def validar_credenciales(self, usuario, password):
        query = """
                SELECT id_admin
                FROM TB_ADMIN
                WHERE usuario_admin = ? AND password_admin = ?
            """

        try:
            self.db.execute(query, usuario, password)
            result = self.db.cursor.fetchone()

            if result:
                print("Credenciales válidas. ID del administrador:", result[0])
                return True
            else:
                print("Credenciales inválidas.")
                return False
        except pyodbc.Error as e:
            print(f"Error al verificar credenciales: {e}")
            return False
