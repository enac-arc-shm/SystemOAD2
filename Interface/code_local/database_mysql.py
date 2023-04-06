import mysql.connector

def conexion_db(host, user, password, database):
    # Conexión a la base de datos
    conection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return conection


def obtain_data_table(conection, table):
    # Obtener registros de una tabla
    mycursor = conection.cursor()
    mycursor.execute(f"SELECT * FROM {table}")
    registros = mycursor.fetchall()
    return registros


def obtain_data_register(conection, table, id):
    # Obtener registro de una tabla con id
    mycursor = conection.cursor()
    mycursor.execute(f"SELECT * FROM {table} WHERE id = {id}")
    registro = mycursor.fetchone()
    return registro


def delete_record_db(conection, table, id):
    # Obtener registro de una tabla con id
    mycursor = conection.cursor()
    mycursor.execute(f"DELETE FROM {table} WHERE id = {id}")
    conection.commit()


def delete_record_db_container(conection, table, id):
    # Obtener registro de una tabla con id
    mycursor = conection.cursor()
    mycursor.execute(f"DELETE FROM {table} WHERE id = '{id}'")
    conection.commit()


def insert_record_cellphone(conection, table, name, number):
    # Obtener registro de una tabla con id
    mycursor = conection.cursor()
    mycursor.execute(f"INSERT INTO {table} (name, number) VALUES ('{name}', {number})")
    registro = mycursor.fetchone()
    conection.commit()
    return registro


def insert_record_service(conection, table, name, priority):
    # Obtener registro de una tabla con id
    mycursor = conection.cursor()
    mycursor.execute(f"INSERT INTO {table} (name, priority) VALUES ('{name}', {priority})")
    registro = mycursor.fetchone()
    conection.commit()
    return registro

def insert_record_container(conection, table, id, name):
    # Obtener registro de una tabla con id
    mycursor = conection.cursor()
    mycursor.execute(f"INSERT INTO {table} (id, name) VALUES ('{id}', '{name}')")
    registro = mycursor.fetchone()
    conection.commit()
    return registro


