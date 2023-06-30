import sqlite3

# Clasa database creata doar ca exemplu, nu am vazut momentan necesitatea dar sunt sigur ca poate fi folosita cu succes in acest proeict.

class Database():
    def __init__(self):
        self.connection = sqlite3.connect('contexto.db')
        self._cursor = self.connection.cursor()
        # Am incercat prima data cu acelas nume la variabila cursor si se pare ca nu merge...? asa ca i-am pus un _ in fata
        # To be tested in the future ?!

    def close(self):
        self.connection.close()

    def execute(self, sql):
        self._cursor.execute(sql)

    def fetch_all(self):
        return self._cursor.fetchall()

    def fetch_one(self):
        return self._cursor.fetchone()

    def query(self, sql):
        self._cursor.execute(sql)
        return self.fetch_all()