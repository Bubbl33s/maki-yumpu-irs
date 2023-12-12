from PyQt5 import QtWidgets


class GenerarPedidoTab():
    def __init__(self, tab, db):
        self.tab = tab
        self.db = db

        self.tab.txt_buscar_cliente_gp.textChanged.connect(self.buscar_cliente)
        
    def buscar_cliente(self):
        codigo_o_nombre = self.tab.txt_buscar_cliente_gp.text()
        result = self.db.buscar_cliente(codigo_o_nombre)

        if codigo_o_nombre and result:
            id_cliente, nombres_cliente, apat_cliente, amat_cliente = result
            self.tab.txt_id_cliente_gp.setText(id_cliente)
            self.tab.txt_nombre_cliente_gp.setText(f"{nombres_cliente} {apat_cliente} {amat_cliente}")
        else:
            # Limpiar los campos si no se encuentra el cliente
            self.tab.txt_id_cliente_gp.clear()
            self.tab.txt_nombre_cliente_gp.clear()
