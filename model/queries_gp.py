import pyodbc
from model.db_conn import Database

class GPQuery:
    def __init__(self):
        self.db = Database()
    
    def buscar_cliente(self, string):
        query = "SELECT id_cliente, nombres_cliente, ap_pat_cliente, ap_mat_cliente FROM TB_CLIENTE WHERE" + \
                "(id_cliente LIKE ?) OR (nombres_cliente LIKE ?) OR (ap_pat_cliente LIKE ?) OR (ap_mat_cliente LIKE ?)"
        args = (f"%{string}%", f"%{string}%", f"%{string}%", f"%{string}%")

        try:
            self.db.execute(query, *args)
            result = self.db.cursor.fetchone()
            return result
        
        except pyodbc.Error as e:
            print(f"Error al buscar el cliente: {e}")
            return None

    def obtener_ultimo_id_prenda(self):
        query = "SELECT TOP 1 id_prenda FROM TB_PRENDA ORDER BY id_prenda DESC"
        try:
            self.db.execute(query)
            result = self.db.cursor.fetchone()
            return result[0] if result else None
        except pyodbc.Error as e:
            print(f"Error al obtener el último id_prenda: {e}")
            return None

    def generar_nuevo_id_prenda(self):
        ultimo_id_prenda = self.obtener_ultimo_id_prenda()
        if ultimo_id_prenda:
            # Obtener la parte numérica del último id_prenda
            num = int(ultimo_id_prenda[4:])
            # Generar el nuevo id_prenda incrementando el número en uno
            nuevo_num = num + 1
            nuevo_id_prenda = f"PREN{str(nuevo_num).zfill(4)}"
            return nuevo_id_prenda
        else:
            # Si no hay registros existentes, empezar desde 1
            return "PREN0001"

    def insertar_prenda(self, desc_prenda):
        nuevo_id_prenda = self.generar_nuevo_id_prenda()
        if nuevo_id_prenda:
            query = "INSERT INTO TB_PRENDA (id_prenda, desc_prenda) VALUES (?, ?)"
            args = (nuevo_id_prenda, desc_prenda)
            try:
                self.db.execute(query, *args)
                self.db.conn.commit()
                print("Prenda insertada correctamente.")
                return nuevo_id_prenda
            except pyodbc.Error as e:
                print(f"Error al insertar la prenda: {e}")
        else:
            print("Error al generar el nuevo id_prenda.")

    def obtener_ultimo_id_pedido(self):
        query = "SELECT TOP 1 id_pedido FROM TB_PEDIDO ORDER BY id_pedido DESC"
        try:
            self.db.execute(query)
            result = self.db.cursor.fetchone()
            return result[0] if result else None
        except pyodbc.Error as e:
            print(f"Error al obtener el último id_pedido: {e}")
            return None

    def generar_nuevo_id_pedido(self):
        ultimo_id_pedido = self.obtener_ultimo_id_pedido()
        if ultimo_id_pedido:
            # Obtener la parte numérica del último id_pedido
            num = int(ultimo_id_pedido[1:])
            # Generar el nuevo id_pedido incrementando el número en uno
            nuevo_num = num + 1
            nuevo_id_pedido = f"P{str(nuevo_num).zfill(7)}"
            return nuevo_id_pedido
        else:
            # Si no hay registros existentes, empezar desde 1
            return "P0000001"

    def insertar_pedido(self, id_cliente, fecha_generacion_pedido, fecha_limite_inicio, fecha_entrega, precio):
        nuevo_id_pedido = self.generar_nuevo_id_pedido()
        if nuevo_id_pedido:
            query = "INSERT INTO TB_PEDIDO (id_pedido, id_cliente, id_admin, fecha_generacion_pedido, fecha_limite_inicio, fecha_entrega, precio) VALUES (?, ?, ?, ?, ?, ?, ?)"
            args = (nuevo_id_pedido, id_cliente, 'ADM00001', fecha_generacion_pedido, fecha_limite_inicio, fecha_entrega, precio)
            try:
                self.db.execute(query, *args)
                self.db.conn.commit()
                print("Pedido insertado correctamente.")
                return nuevo_id_pedido
            except pyodbc.Error as e:
                print(f"Error al insertar el pedido: {e}")
        else:
            print("Error al generar el nuevo id_pedido.")
            return None

            
    def insertar_detalle_pedido(self, id_pedido, id_prenda, cantidad_prenda, id_pantone):
        query = """
            INSERT INTO TB_DETALLE_PEDIDO (id_pedido, id_prenda, cantidad_prenda, id_pantone)
            VALUES (?, ?, ?, ?);
        """

        args = (id_pedido, id_prenda, cantidad_prenda, id_pantone)

        try:
            self.db.execute(query, *args)
            self.db.conn.commit()
            print("Detalle del pedido insertado correctamente.")
        except pyodbc.Error as e:
            print(f"Error al insertar detalle del pedido: {e}")
