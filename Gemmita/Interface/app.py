from flask import Flask
from flask import render_template
import matplotlib.pyplot as plt
import numpy as np

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
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange
import time
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dhcp')
def docker_dhcp():
    return render_template('dhcp.html')


@app.route('/whatsapp')
def whatsapp():
    return render_template('whatsapp.html')

@app.route('/chart-data')
#Aquí se mandan los datos para generar una grafica con numeros aleatorios
def chart_data():
    def generate_random_data():
        while True:
            json_data = json.dumps(
                {
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                    'value': random.random() * 100})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
    return response

@app.route('/chart-data2')
#Aquí se mandan los datos para generar una grafica con el porcentaje de CPU usada, la cual se manda cada 4 segundos
def chart_data2():
    def display_usage(cpu_usage,mem_usage,bars=50):
        cpu_use = (cpu_usage) 
        mem_use = (mem_usage/100.0)     
        return cpu_use
    def generate_random_data2():
        while True:
            cpuu=psutil.cpu_percent()
            print(cpuu)
            json_data2 = json.dumps(
                {
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                    'value': cpuu})
            yield f"data:{json_data2}\n\n"
            time.sleep(4)

    response = Response(stream_with_context(generate_random_data2()), mimetype="text/event-stream")
    return response
if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True, port=4001)