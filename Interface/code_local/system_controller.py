import code_local.database_mysql
import code_local.conexion_ssh
from code_local.messages_heyoo import WhatsappService

conection_db = code_local.database_mysql.conexion_db(host='localhost', user='user', password='ser1234gio', database='systemoad_db')
conection_ssh = code_local.conexion_ssh.conection(host='localhost', user='enac-ar-shm', psswd='P0wd3r!', portssh=22)

def obtain_mysql_data_cellphones():
    return code_local.database_mysql.obtain_data_table(conection_db, 'cellphones')

def obtain_mysql_data_services():
    return code_local.database_mysql.obtain_data_table(conection_db, 'services')

def obtain_ssh_data_services():
    return code_local.conexion_ssh.get_services_list(conection_ssh)

def obtain_ssh_containers():
    return code_local.conexion_ssh.get_containers_list(conection_ssh)

def obtain_mysql_containers():
    return code_local.database_mysql.obtain_data_table(conection_db, 'containers')

def system_message(id, message):
    cellphone_user = code_local.database_mysql.obtain_data_register(conection_db, 'cellphones', id)
    send_message(cellphone=f'{cellphone_user[2]}', server='ALMA', message=message)

def send_message(cellphone, server, message):
    WhasappMessageLocal = WhatsappService(cellphone, server)
    if message is None:
        WhasappMessageLocal.sendMessage('Mensaje de prueba')
    else:
        WhasappMessageLocal.sendMessage(message)

def system_delete_cellphone(id):
    code_local.database_mysql.delete_record_db(conection_db, 'cellphones', id)

def system_insert_cellphone(name, number):
    code_local.database_mysql.insert_record_cellphone(conection_db, 'cellphones', name, number)

def system_insert_service(name, priority):
    code_local.database_mysql.insert_record_service(conection_db, 'services', name, priority)    

def system_delete_service(id):
    code_local.database_mysql.delete_record_db(conection_db, 'services', id)

def system_insert_container(id, name):
    code_local.database_mysql.insert_record_container(conection_db, 'containers', id, name)    

def system_delete_container(id):
    code_local.database_mysql.delete_record_db_container(conection_db, 'containers', id)