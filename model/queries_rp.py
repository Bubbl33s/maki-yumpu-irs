import pyodbc
from model.db_conn import Database

class RPQuery:
    def __init__(self):
        self.db = Database()
    
    def buscar_cliente(self, string):
        query = """
                SELECT
                    c.id_cliente,
                    c.nombres_cliente,
                    c.ap_pat_cliente,
                    c.ap_mat_cliente,
                    p.id_pedido,
                    p.fecha_generacion_pedido,
                    p.precio
                FROM
                    TB_CLIENTE c
                JOIN
                    TB_PEDIDO p ON c.id_cliente = p.id_cliente
                WHERE
                    (p.id_cliente LIKE ?) OR (c.nombres_cliente LIKE ?) OR
                    (ap_pat_cliente LIKE ?) OR (ap_mat_cliente LIKE ?);
                """
        args = (f"%{string}%", f"%{string}%", f"%{string}%", f"%{string}%")

        try:
            self.db.execute(query, *args)
            result = self.db.cursor.fetchall()
            return result
        
        except pyodbc.Error as e:
            print(f"Error al buscar el cliente: {e}")
            return None

    def buscar_pedido(self, string):
        query = """
                SELECT
                    dp.id_pedido,
                    pr.id_prenda,
                    pr.desc_prenda,
                    dp.cantidad_prenda,
                    dp.id_pantone
                FROM
                    TB_DETALLE_PEDIDO dp
                JOIN
                    TB_PRENDA pr ON dp.id_prenda = pr.id_prenda
                WHERE
                    dp.id_pedido LIKE ?;
                """
        
        args = (f"%{string}%",)
        
        try:
            self.db.execute(query, *args)
            result = self.db.cursor.fetchall()
            return result
        
        except pyodbc.Error as e:
            print(f"Error al buscar pedido: {e}")
            return None
