DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'nombre_de_tu_base_de_datos',
        'HOST': 'localhost\\SQLEXPRESS',  # Para SQL Server Express
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'trusted_connection': 'yes',  # Autenticación de Windows
        },
    }
}