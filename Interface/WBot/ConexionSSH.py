import paramiko
from paramiko.client import SSHClient
from colorama import Fore

class ConexionSSH():

    def __init__(self, host, user, psswd, portssh):

        conexion = paramiko.SSHClient()
        conexion.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conexion.connect(host, username=user, password=psswd, port=portssh, timeout=10)
        print(Fore.GREEN + "[+] Conexión exitosa" + Fore.WHITE)
        self.conexion = conexion


    def CommandQuery(self, command):
        conexion = self.conexion
        stdin, stdout, stderr = conexion.exec_command(command)
        return stdout.read().decode("utf-8")
