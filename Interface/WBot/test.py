from Send_Msj import WhatsappService
from ConexionSSH import ConexionSSH

if __name__ == "__main__":
    WhasappMessageLocal = WhatsappService('527731922477', 'ALMA')
    #WhasappMessageLocal.sendReplyButtonServer()
    #WhasappMessageLocal.sendButtonService('http', 'dead')
    newConexion = ConexionSSH(host='ssh-systemoad2.alwaysdata.net', user='systemoad2_sergio', psswd='ser1234gio', portssh=22)
    print (newConexion.CommandQuery("cat www2/comandos.txt"))