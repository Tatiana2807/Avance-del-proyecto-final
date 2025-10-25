# script_crear_db.py
import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'UID=tu_usuario;'
    'PWD=tu_contraseña;'
    'Trusted_Connection=yes;'
)
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("CREATE DATABASE GestinClinicaDB")
print("Base de datos creada exitosamente")
cursor.close()
conn.close()