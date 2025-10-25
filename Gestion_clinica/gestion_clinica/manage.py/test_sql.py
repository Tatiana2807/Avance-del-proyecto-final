import pyodbc

try:
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"  # o localhost\\SQLEXPRESS
        "DATABASE=GestionClinicaDB;"
        "UID=sa;"
        "PWD=TuContraseña;"
    )
    print("✅ Conexión exitosa con SQL Server")
except Exception as e:
    print("❌ Error:", e)
