import pyodbc

class Database:
    # SINGLETON
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        
        return cls._instance
    
    # CONNECTION STRING
    def __init__(self):
        self.server = 'BUBBLES'
        self.database = 'MakiYumpuSAC'
        self.connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;"

        if not hasattr(self, 'conn') or self.conn is None:
            self.connect()
    
    # CONNECTION TO DB
    def connect(self):
        try:
            self.conn = pyodbc.connect(self.connection_string)
            print("Succesfull conn.")
        except pyodbc.Error as error:
            print("Error al conectar a la base de datos:", error)
            return None

        self.cursor = self.conn.cursor()
    
    # QUERY EXECUTIONS
    def execute(self, query, *args):
        try:
            if not self.conn:
                self.connect()
            self.cursor.execute(query, *args)
        except pyodbc.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        
    # CLOSE CONNECTION
    def close_connection(self):
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()
            print("Closed connection")
            self.conn = None
    
    def __del__(self):
        self.close_connection()
