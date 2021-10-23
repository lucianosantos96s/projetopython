import sqlite3
from sqlite3.dbapi2 import Cursor

class cnpjs(object):

    def __init__(self):
        cnpj = None
        razaoSocial = None
        email = None

    def criaTabela(self):
        conn = sqlite3.connect("CLIENTES.db")
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS CLIENTES(
                CNPJ CHAR (18),
                RAZAOSOCIAL CHAR (100),
                EMAIL CHAR (30)
            )
         ''')

        conn.commit()

    def salvar(self):
        self.criaTabela()
        conn = sqlite3.connect("CLIENTES.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO CLIENTES VALUES('%s', '%s','%s')" % (self.cnpj, self.razaoSocial, self.email))
        conn.commit()

    def listarCNPJ(self):
        conn = sqlite3.connect("CLIENTES.db")
        cursor = conn.cursor()
        sql = '''
            SELECT rowid, * FROM CLIENTES ORDER BY RAZAOSOCIAL
        '''
        cursor.execute(sql)

        for i in cursor.fetchall():
            print(i)
