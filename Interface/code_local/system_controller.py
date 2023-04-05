import code_local.database_mysql
from code_local.messages_heyoo import WhatsappService

conection = code_local.database_mysql.conexion_db(host='localhost', user='user', password='ser1234gio', database='systemoad_db')

def obtain_mysql_data_cellphones():
    return code_local.database_mysql.obtain_data_table(conection, 'cellphones')

def obtain_mysql_data_services():
    return code_local.database_mysql.obtain_data_table(conection, 'services')

def system_message(id, message):
    cellphone_user = code_local.database_mysql.obtain_data_register(conection, 'cellphones', id)
    send_message(cellphone=f'{cellphone_user[2]}', server='ALMA', message=message)

def send_message(cellphone, server, message):
    WhasappMessageLocal = WhatsappService(cellphone, server)
    if message is None:
        WhasappMessageLocal.sendMessage('Mensaje de prueba')
    else:
        WhasappMessageLocal.sendMessage(message)

def system_delete_cellphone(id):
    code_local.database_mysql.delete_record_cellphone(conection, 'cellphones', id)

def system_insert_cellphone(name, number):
    code_local.database_mysql.insert_record_cellphone(conection, 'cellphones', name, number)

if __name__ == '__main__':
    cellphones = obtain_mysql_data_cellphones()
