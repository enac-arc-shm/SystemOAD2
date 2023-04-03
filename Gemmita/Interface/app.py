from flask import Flask, config, render_template, request, Response ,stream_with_context
import time
import json
import psutil 
from datetime import datetime
import random
from random import random
from random import random, randrange
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