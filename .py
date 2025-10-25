import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=GestionClinicaDB;"
    "UID=sa;"
    "PWD=TuContraseña;"
)
print("Conexión exitosa ✅")


import pyodbc
print(pyodbc.drivers())