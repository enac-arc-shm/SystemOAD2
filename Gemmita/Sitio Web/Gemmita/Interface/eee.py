import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange
import time
import psutil
import paramiko
list_users = []
def conection():
    ip = "192.168.1.90"
    user = 'root'
    psswd = 'agmv'
    portssh = '22'
    conection = paramiko.SSHClient()
    conection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conection.connect("192.168.1.48", username=user,password=psswd, port=portssh, timeout=10)
    return conection

def query_device(conection, command):
    stdin, stdout, stderr = conection.exec_command(command)
    return stdout.read().decode("utf-8")
def get_list_users():
    return list_users
def set_list_users(data):
    global list_users
    list_users.append(data)

def display_usage(cpu_usage,mem_usage,bars=50):
    cpu_use = (cpu_usage) 
    mem_use = (mem_usage/100.0)     
    print(cpu_use) 
    print(mem_use)

    while True:
        display_usage(psutil.cpu_percent(),psutil.virtual_memory().percent,30)
        time.sleep(1.2)


def datos():
    months=['dic','jan','feb','mar','apr']
    for mes in months:
        users = 'cat /var/log/httpd/access_log | grep "HTTP/1.*\" 200 | grep {} '.format(mes)
        print(users)

def datoss():
    jsonnn={}
    connec = conection()
    months=['Dic','Jan','Feb','Mar','Apr']
    for mes in months:
        cad='cat /var/log/httpd/access_log | grep "HTTP" | grep "200" | grep {} | wc -l'.format(mes)
        users = query_device(connec,cad)
        #print(users)
        #print('{}'.format(mes),':', '{}'.format(users))
        #users='{}'.format(users)
        #list_users.append(users.rstrip())
        #valll='{}'.format(mes),':','{}'.format(users)
        #valll=mes,':',users
        #print(valll)
        #jsonnn.setdefault(mes,int(users.rstrip()))
        jsonnn.setdefault('mes : {}'.format(mes),'value :{}'.format(int(users.rstrip())))
    #print(list_users)
        #jsonnn={'mes':mes,'value':int(users.rstrip())}
    print(jsonnn)
def datooss():
        #while True:
    connec = conection()
    months=['Dic','Jan','Feb','Mar','Apr']
    valuesm=[]
    for mes in months:
        cad='cat /var/log/httpd/access_log | grep "HTTP" | grep "200" | grep {} | wc -l'.format(mes)
        users = query_device(connec,cad)
        users='{}'.format(int(users.rstrip()))
        valuesm.append(users)
        #jsonnn.setdefault('mes : {}'.format(mes),'value :{}'.format(int(users.rstrip())))
        #print(jsonnn)
        #time.sleep(5)
    #response = Response(stream_with_context(datoss()), mimetype="text/event-stream")
    #jsonify(jsonnn)
    jsonnn={
        "mes":months,
        "values":valuesm
    }
    print(jsonnn)
    #data = {
     #   "labels": ["January", "February", "March", "April", "May", "June", "July"],
      #  "values": [10, 20, 30, 40, 50, 60, 70]
    #}
    """jsonnn={
      "mes":['Dic',' Jan',' Feb',' Mar',' Apr'],
      "value":[0,0,0,0,4]  
    }"""
    

if __name__ == '__main__':
    #cadd='cat /var/log/httpd/access_log | grep "HTTP/1.*\" 200" | grep "Apr" | wc -l'
    #connec = conection()
    #users = query_device(connec,'cat /var/log/httpd/access_log | grep "HTTP" | grep "200" | grep "Apr" | wc -l')
    connec = conection()
    days=[]
    fecha_actual = datetime.now()
    fecha_actual=fecha_actual.strftime('%B')
    for i in range (5):
        cad='date -d "{} day ago" "+%e"'.format(i)
        dayss = query_device(connec,cad)
        dayss='{} {}'.format(fecha_actual[0:3],dayss.rstrip())
       # print(dayss)
        days.append(dayss)
    
    valuesr=[]
    for day in days:
        cad='cat /var/log/messages | grep "named.*error" | grep "{}" | wc -l'.format(day)
        resol = query_device(connec,cad)
        resol='{}'.format(resol.rstrip())
        valuesr.append(resol)
    jsonnn={
        "dias":days,
        "value":valuesr
    }
    print(jsonnn)
    """datooss()
    def datooss():
        #while True:
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
    print(jsonnn)
    #jsonnn={'mes : Dic': 'value :0', 'mes : Jan': 'value :0', 'mes : Feb': 'value :0', 'mes : Mar': 'value :0', 'mes : Apr': 'value :4'}

    return jsonify(jsonnn)
    
    
    
    
@app.route('/chart-data4')
#Aquí se mandan los datos para generar una grafica con el porcentaje de CPU usada, la cual se manda cada 4 segundos
def chart_data4():
    def display_usage(cpu_usage,mem_usage,bars=50):
        cpu_use = (cpu_usage) 
        mem_use = (mem_usage/100.0)     
        return cpu_use
    def generate_random_data4():
        while True:
            cpuu=psutil.cpu_percent()
           # print(cpuu)
            json_data2 = json.dumps(
                {
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                    'value': cpuu})
            yield f"data:{json_data2}\n\n"
            time.sleep(5)
            #print(json_data2)
    response = Response(stream_with_context(generate_random_data4()), mimetype="text/event-stream")
    return response"""
    ------------------
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
    #fecha_actual = datetime.now()
    #fecha_actual=fecha_actual.strftime('%B')
    #for i in range (5):
    #    cad='date -d "{} day ago" "+%e"'.format(i)
    #    dayss = query_device(connec,cad)
    #    dayss='{} {}'.format(fecha_actual[0:3],dayss.rstrip())
    #   # print(dayss)
    #    days.append(dayss)
    months=["Dic","Jan","Feb","Mar","Apr"]
    valuesr=[]
    #for day in days:
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
        #while True:
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
    #jsonnn={'mes : Dic': 'value :0', 'mes : Jan': 'value :0', 'mes : Feb': 'value :0', 'mes : Mar': 'value :0', 'mes : Apr': 'value :4'}

    return jsonify(jsonnn)

@app.route('/chart-data6')
def datooss6():
        #while True:
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
        #while True:
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