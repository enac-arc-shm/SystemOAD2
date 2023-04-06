import mysql.connector

# Configuración de la conexión a la base de datos
config = {
    'user': 'user',
    'password': 'ser1234gio',
    'host': 'localhost',
    'port': '3306',
    'database': 'systemoad_db'
}

# Conexión a la base de datos
try:
    conn = mysql.connector.connect(**config)
    print("Conexión exitosa a la base de datos")
except mysql.connector.Error as err:
    print(f"Error de conexión a la base de datos: {err}")
    exit(1)

# Creación de la tabla
try:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cellphones (
            id INT(11) NOT NULL AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            number BIGINT NOT NULL,
            PRIMARY KEY (id)
        ) ENGINE=InnoDB
    """)
    print("Tabla cellphones creada exitosamente")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS services (
            id INT(11) NOT NULL AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            priority INT NOT NULL,
            PRIMARY KEY (id)
        ) ENGINE=InnoDB
    """)
    print("Tabla servicescreada exitosamente")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS containers (
            id VARCHAR(20) NOT NULL,
            name VARCHAR(100) NOT NULL,
            PRIMARY KEY (id)
        ) ENGINE=InnoDB
    """)
    print("Tabla containers exitosamente")

except mysql.connector.Error as err:
    print(f"Error al crear la tabla: {err}")
    exit(1)
    
# Cierre de la conexión
cursor.close()
conn.close()
