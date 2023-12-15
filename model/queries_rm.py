import pyodbc
from model.db_conn import Database

class RMQuery:
    def __init__(self):
        self.db = Database()
    
    def obtener_materiales(self):
        query = "SELECT desc_material FROM TB_MATERIAL"

        try:
            self.db.execute(query)
            resultados = self.db.cursor.fetchall()
            return [material[0] for material in resultados]  # Devuelve una lista de descripciones de materiales
        except pyodbc.Error as e:
            print(f"Error al obtener materiales: {e}")
            return []
