import sqlite3

def get_conexion():
    conexion = sqlite3.connect("clinicadb.sqlite3")
    conexion.row_factory = sqlite3.Row
    return conexion