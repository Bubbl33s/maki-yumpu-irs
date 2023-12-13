from PyQt5 import QtWidgets

from model.queries_rp import RPQuery


class RastrearPedidoTab:
    def __init__(self, tab):
        self.tab = tab
        self.queries = RPQuery()
        
        self.tab.txt_buscar_cliente_rp.textChanged.connect(self.buscar_pedido_cliente)
        self.tab.txt_buscar_rp.textChanged.connect(self.buscar_pedido)
        
    def buscar_pedido_cliente(self):
        codigo_o_nombre = self.tab.txt_buscar_cliente_rp.text()
        result = self.queries.buscar_cliente(codigo_o_nombre)

        # Limpiar la tabla antes de agregar nuevos datos
        self.tab.tbl_pedido_cliente_rp.setRowCount(0)

        if codigo_o_nombre and result:
            for row_data in result:
                # Agregar una nueva fila a la tabla
                row_position = self.tab.tbl_pedido_cliente_rp.rowCount()
                self.tab.tbl_pedido_cliente_rp.insertRow(row_position)

                # Realizar concatenación de nombres y apellidos
                nombres_apellidos = ' '.join(row_data[1:4])

                # Insertar datos directamente en las columnas
                self.tab.tbl_pedido_cliente_rp.setItem(row_position, 0,
                                                        QtWidgets.QTableWidgetItem(str(row_data[0])))
                self.tab.tbl_pedido_cliente_rp.setItem(row_position, 1,
                                                        QtWidgets.QTableWidgetItem(nombres_apellidos))
                self.tab.tbl_pedido_cliente_rp.setItem(row_position, 2,
                                                        QtWidgets.QTableWidgetItem(str(row_data[4])))
                self.tab.tbl_pedido_cliente_rp.setItem(row_position, 3,
                                                        QtWidgets.QTableWidgetItem(str(row_data[5])))
                self.tab.tbl_pedido_cliente_rp.setItem(row_position, 4,
                                                        QtWidgets.QTableWidgetItem(str(format(row_data[6], ".2f"))))
        else:
            # Limpiar la tabla si no hay resultados
            self.tab.tbl_pedido_cliente_rp.setRowCount(0)

    def buscar_pedido(self):
        codigo = self.tab.txt_buscar_rp.text()
        result = self.queries.buscar_pedido(codigo)
        
        self.tab.tbl_detalle_pedido_rp.setRowCount(0)
        
        if codigo and result:
            for row_data in result:
                row_position = self.tab.tbl_detalle_pedido_rp.rowCount()
                self.tab.tbl_detalle_pedido_rp.insertRow(row_position)
                
                for col, data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(data))
                    self.tab.tbl_detalle_pedido_rp.setItem(row_position, col, item)
        else:
            self.tab.tbl_detalle_pedido_rp.setRowCount(0)
    