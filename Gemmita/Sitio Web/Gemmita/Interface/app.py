from flask import Flask, jsonify
from flask import render_template
#import matplotlib.pyplot as plt
#import numpy as np

from flask import Flask, config, render_template, request, Response ,stream_with_context
import pandas as pd
import json
import psutil
from time import time
from flask import Flask, render_template, make_response
from random import random
import time
import random 
from datetime import datetime
#import matplotlib.pyplot as plt
from datetime import datetime
#from matplotlib import pyplot
#from matplotlib.animation import FuncAnimation
from random import randrange
import time
import paramiko

app = Flask(__name__)
list_users = []
def conection():
    ip = "192.168.49.185"
    user = 'root'
    psswd = 'agmv'
    portssh = '22'
    conection = paramiko.SSHClient()
    conection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conection.connect("192.168.43.137", username=user,password=psswd, port=portssh, timeout=10)
    return conection
def query_device(conection, command):
    stdin, stdout, stderr = conection.exec_command(command)
    return stdout.read().decode("utf-8")
def get_list_users():
    return list_users

def set_list_users(data):
    global list_users
    list_users.append(data)

@app.route('/')
def home():
    #render_template('index.html') pqsiiiii
    return render_template('index.html')

@app.route('/norm')
def home2():
    return render_template('_index.html')

@app.route('/form')
def jjjj():
    return render_template('bc_tabs.html')

 




@app.route('/dhcp')
def docker_dhcp():
    return render_template('dhcp.html')


@app.route('/whatsapp')
def whatsapp():
    return render_template('whatsapp.html')

@app.route('/chart-data1')
def datooss1():
    connec = conection()
    months=["Dic","Jan","Feb","Mar","Apr"]
    valuessd=[]
    for mes in months:
        cad='cat /var/log/messages | grep "DHCPDISCOVER" | grep "{}" | wc -l'.format(mes)
        resol = query_device(connec,cad)
        resol='{}'.format(resol.rstrip())
        valuessd.append(resol)
    jsonnn={
        "mes":months,
        "value":valuessd
    } 
    print("Primer json")
    print(jsonnn)
    return jsonify(jsonnn)

@app.route('/chart-data2')
def datooss2():
    connec = conection()
    months=["Dic","Jan","Feb","Mar","Apr"]
    valuesad=[]
    for mes in months:
        cad='cat /var/log/messages | grep "DHCPACK" | grep "{}" | wc -l'.format(mes)
        resol = query_device(connec,cad)
        resol='{}'.format(resol.rstrip())
        valuesad.append(resol)
    jsonnn={
        "mes":months,
        "value":valuesad
    }
    print("Segundo json")
    print(jsonnn)
    return jsonify(jsonnn)

@app.route('/chart-data3')
def datooss3():
    connec = conection()
    months=["Dic","Jan","Feb","Mar","Apr"]
    valuesm=[]
    for mes in months:
        cad='cat /var/log/messages | grep "stopping" | grep "{}" | wc -l'.format(mes)
        resol = query_device(connec,cad)
        resol='{}'.format(resol.rstrip())
        valuesm.append(resol)
    jsonnn={
        "mes":months,
        "value":valuesm
    }
    print("Tercer json")
    print(jsonnn)
    return jsonify(jsonnn)

@app.route('/chart-data4')
def datooss4():
    connec = conection()
    days=[]
    months=["Dic","Jan","Feb","Mar","Apr"]
    valuesr=[]
    for mes in months:
        cad='cat /var/log/messages | grep "named.*error" | grep "{}" | wc -l'.format(mes)
        resol = query_device(connec,cad)
        resol='{}'.format(resol.rstrip())
        valuesr.append(resol)
    jsonnn={
        "mes":months,
        "value":valuesr
    }
    print("Cuarto json")
    print(jsonnn)
    return jsonify(jsonnn)

@app.route('/chart-data5')
def datooss():
    connec = conection()
    months=["Dic","Jan","Feb","Mar","Apr"]
    valuesm=[]
    for mes in months:
        cad='cat /var/log/httpd/access_log | grep "HTTP" | grep "404" | grep {} | wc -l'.format(mes)
        users = query_device(connec,cad)
        users='{}'.format(int(users.rstrip()))
        valuesm.append(users)
    jsonnn={
        "mes":months,
        "value":valuesm
    }
    print("Quinto json")
    print(jsonnn)
    return jsonify(jsonnn)

@app.route('/chart-data6')
def datooss6():
    connec = conection()
    months=["Dic","Jan","Feb","Mar","Apr"]
    valuesm=[]
    for mes in months:
        cad='cat /var/log/httpd/access_log | grep "HTTP" | grep "200" | grep {} | wc -l'.format(mes)
        users = query_device(connec,cad)
        users='{}'.format(int(users.rstrip()))
        valuesm.append(users)
    jsonnn={
        "mes":months,
        "value":valuesm
    }
    print("Sexto json")
    print(jsonnn)
    return jsonify(jsonnn)

@app.route('/chart-data7')
def datooss7():
    connec = conection()
    usersserv=["ana","vero","agmv"]
    valuesu=[]
    for user in usersserv:
        cad='cat /var/log/xferlog-20230221 | grep "{} ftp" | wc -l'.format(user)
        users = query_device(connec,cad)
        users='{}'.format(int(users.rstrip()))
        valuesu.append(users)
    jsonnn={
        "user":usersserv,
        "value":valuesu
    }
    print("Séptimo json")
    print(jsonnn)
    return jsonify(jsonnn)
if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True, port=4001)