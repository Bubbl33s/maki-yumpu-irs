from PyQt5 import QtWidgets

from model.queries_rm import RMQuery


class ReporteMaterialTab:
    def __init__(self, tab):
        self.tab = tab
        self.queries = RMQuery()
        
        self.llenar_materiales()

    def llenar_materiales(self):
        materiales = self.queries.obtener_materiales()
        self.tab.cbo_material_rm.addItems(materiales)
