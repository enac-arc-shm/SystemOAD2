import paramiko
import os
import sys
import getpass
import time
from colorama import Fore
from paramiko.client import SSHClient
import re 


def get_services_list(con):
    services_enabled_local = query_device(con, "systemctl list-unit-files --type service --all | grep enabled")
    list_services = services_analisys(services_enabled_local)
    return list_services

def get_containers_list(con):
    local_containers = query_device(con, "docker ps -aq")
    list_containers = containers_analisys(con, local_containers)
    return list_containers


def query_device(conection, command):
    #Realice execute ssh command 
    stdin, stdout, stderr = conection.exec_command(command)
    return stdout.read().decode("utf-8")


def conection(host, user, psswd, portssh):
    #Create instan SSH
    conection = paramiko.SSHClient()
    #Configuration paramiko policy
    conection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #Autentucation conect 
    conection.connect(host, username=user,password=psswd, port=portssh, timeout=10)
    print(Fore.GREEN + "[+] Conexión ssh exitosa" + Fore.WHITE)
    return conection


def services_analisys(services):
    diccionario_services = {}
    lista_servicios = []
    contador = 0
    services = re.split('\s', services)
    for data in services:
        if data != '':
            contador += 1
            if contador == 1:
                diccionario_services["service"] = data
            elif contador == 2:
                diccionario_services["status"] = data
            elif contador == 3:
                diccionario_services["Vendor"] = data
                lista_servicios.append(diccionario_services.copy())
                contador = 0
    return lista_servicios


def containers_analisys(con, containers):
    diccionario_containers = {}
    lista_containers = []
    lista_containers_id = re.split('\n', containers)
    lista_containers_id = list(filter(bool, lista_containers_id))
    for container in lista_containers_id:
        diccionario_containers['ID'] = container
        command = "docker inspect --format='{{.Created}}' " + str(container)
        diccionario_containers['CREATED'] = query_device(con, command)
        command = "docker inspect --format='{{.Name}}' " + str(container)
        diccionario_containers['NAME'] = query_device(con, command)
        command = "docker inspect --format='{{.State.Status}}' " + str(container)
        diccionario_containers['STATUS'] = query_device(con, command)
        command = "docker inspect --format='{{.NetworkSettings.Ports}}' " + str(container)
        diccionario_containers['PORTS'] = query_device(con, command)
        lista_containers.append(diccionario_containers.copy())
    return lista_containers


if __name__ == '__main__':
    conection_ssh = conection(host='localhost', user='enac-ar-shm', psswd='P0wd3r!', portssh=22)
    list_containers = (get_containers_list(conection_ssh))
    print(list_containers)