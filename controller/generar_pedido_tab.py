from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate

from model.queries_gp import GPQuery


class GenerarPedidoTab:
    def __init__(self, tab):
        self.tab = tab
        self.queries = GPQuery()

        self.tab.txt_buscar_cliente_gp.textChanged.connect(self.buscar_cliente)
        self.tab.btn_agregar_prenda_gp.clicked.connect(self.agregar_prenda)
        self.tab.btn_cancelar_gp.clicked.connect(self.limpiar_campos)
        self.tab.btn_generar_gp.clicked.connect(self.generar_pedido)
        self.limpiar_campos()
        
    def buscar_cliente(self):
        codigo_o_nombre = self.tab.txt_buscar_cliente_gp.text()
        result = self.queries.buscar_cliente(codigo_o_nombre)

        if codigo_o_nombre and result:
            id_cliente, nombres_cliente, apat_cliente, amat_cliente = result
            self.tab.txt_id_cliente_gp.setText(id_cliente)
            self.tab.txt_nombre_cliente_gp.setText(f"{nombres_cliente} {apat_cliente} {amat_cliente}")
        else:
            self.tab.txt_id_cliente_gp.clear()
            self.tab.txt_nombre_cliente_gp.clear()

    def agregar_prenda(self):
        row_pos = self.tab.tbl_pedido_gp.rowCount()
        self.tab.tbl_pedido_gp.insertRow(row_pos)
        
        data = [self.tab.txt_dec_prenda_gp.toPlainText(),
                self.tab.spb_cantidad_gp.value(), self.tab.txt_color_prenda_gp.text(),
                self.tab.cbo_umedida_gp.currentText()]
        
        for col, dato in enumerate(data):
            self.tab.tbl_pedido_gp.setItem(row_pos, col, QtWidgets.QTableWidgetItem(str(dato)))\
        
        self.limpiar_campos_prenda()
    
    def generar_pedido(self):
        # Obtener datos del cliente
        id_cliente = self.tab.txt_id_cliente_gp.text()

        # Insertar datos en la tabla TB_PEDIDO
        fecha_generacion_pedido = QDate.currentDate().toString("yyyy-MM-dd")
        fecha_limite_inicio = self.tab.date_inicio_gp.date().toString("yyyy-MM-dd")
        fecha_entrega = self.tab.date_entrega_gp.date().toString("yyyy-MM-dd")
        precio = self.tab.spb_precio_gp.value()

        id_pedido = self.queries.insertar_pedido(
            id_cliente, fecha_generacion_pedido, fecha_limite_inicio, fecha_entrega, precio)

        if id_pedido:
            # Insertar datos en la tabla TB_DETALLE_PEDIDO
            for row in range(self.tab.tbl_pedido_gp.rowCount()):
                desc_prenda = self.tab.tbl_pedido_gp.item(row, 0).text()
                cantidad_prenda = int(self.tab.tbl_pedido_gp.item(row, 1).text())
                id_pantone = self.tab.tbl_pedido_gp.item(row, 2).text()

                # Insertar datos en la tabla TB_PRENDA
                id_prenda = self.queries.insertar_prenda(desc_prenda)

                # Insertar datos en la tabla TB_DETALLE_PEDIDO
                self.queries.insertar_detalle_pedido(id_pedido, id_prenda, cantidad_prenda, id_pantone)

        # Limpiar campos después de generar el pedido
        self.limpiar_campos()
    
    # LIMPIAR CAMPOS
    def limpiar_campos_prenda(self):
        self.tab.txt_dec_prenda_gp.clear()
        self.tab.spb_cantidad_gp.setValue(0)
        self.tab.txt_color_prenda_gp.clear()
        self.tab.cbo_umedida_gp.setCurrentIndex(0)
    
    def limpiar_campos(self):
        self.tab.txt_buscar_cliente_gp.clear()
        self.tab.txt_id_cliente_gp.clear()
        self.tab.txt_nombre_cliente_gp.clear()
        self.limpiar_campos_prenda()
        self.tab.tbl_pedido_gp.setRowCount(0)
        self.tab.txt_descripcion_gp.clear()
        self.tab.txt_especificaciones_gp.clear()
        self.tab.date_inicio_gp.setDate(QDate.currentDate())
        self.tab.date_entrega_gp.setDate(QDate.currentDate())
        