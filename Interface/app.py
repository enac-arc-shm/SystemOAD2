from flask import Flask, render_template, redirect, url_for, request,jsonify
from code_local.system_controller import (
    obtain_mysql_data_cellphones, 
    send_message, system_message, 
    system_delete_cellphone, 
    system_insert_cellphone, 
    obtain_mysql_data_services, 
    obtain_ssh_data_services, 
    system_delete_service,
    system_insert_service,
    obtain_ssh_containers,
    obtain_mysql_containers,
    system_insert_container,
    system_delete_container
)
from code_local.conexion_ssh import generales, chartdata7

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dhcp')
def docker_dhcp():
    return render_template('dhcp.html')


@app.route('/whatsapp')
def whatsapp():
    cellphones = obtain_mysql_data_cellphones()
    services_db = obtain_mysql_data_services()
    services_ssh = obtain_ssh_data_services()
    containers_ssh = obtain_ssh_containers()
    containers_db = obtain_mysql_containers()
    return render_template('whatsapp.html', cellphones=cellphones, services_db=services_db, services_ssh=services_ssh, containers_ssh=containers_ssh, containers_db=containers_db)


@app.route('/test_message/<int:id>')
def test_message(id):
    system_message(id, message=None)
    return redirect(url_for('whatsapp'))


@app.route('/writte_message', methods=['POST'])
def writte_message():
    user_recibe = request.form['user_recibe']
    message = request.form['message']
    id_local = request.form['id']
    print("valor local", id_local)
    system_message(id_local, message=message)
    return redirect(url_for('whatsapp'))


@app.route('/delete_cellphone/<int:id>')
def delete_cellphone(id):
    system_delete_cellphone(id)
    return redirect(url_for('whatsapp'))


@app.route('/delete_service/<int:id>')
def delete_service(id):
    system_delete_service(id)
    return redirect(url_for('whatsapp'))


@app.route('/delete_container/<string:id>')
def delete_container(id):
    system_delete_container(id)
    return redirect(url_for('whatsapp'))


@app.route('/insert_service', methods=['POST'])
def insert_service():
    name = request.form['name']
    priority = request.form['priority']
    system_insert_service(name, priority)
    return redirect(url_for('whatsapp'))


@app.route('/insert_cellphone', methods=['POST'])
def insert_cellphone():
    name = request.form['name']
    number = request.form['number']
    system_insert_cellphone(name, number)
    return redirect(url_for('whatsapp'))


@app.route('/insert_container/<string:id>/<string:name>')
def insert_container(id, name):
    system_insert_container(id, name)
    return redirect(url_for('whatsapp'))

###################3
@app.route('/chart-data1')
def chartdata1():
    cad='cat /var/log/messages | grep "DHCPDISCOVER" | grep "'
    return jsonify(generales(cad))

@app.route('/chart-data2')
def chartdata2():
    cad='cat /var/log/messages | grep "DHCPACK" | grep '
    return jsonify(generales(cad))
   
@app.route('/chart-data3')
def chartdata3():
    cad='cat /var/log/messages | grep "stopping" | grep '
    return jsonify(generales(cad))

@app.route('/chart-data4')
def chartdata4():
    cad='cat /var/log/messages | grep "named.*error" | grep '
    return jsonify(generales(cad))

@app.route('/chart-data5')
def chartdata5():
    cad='cat /var/log/httpd/access_log | grep "HTTP" | grep "404" | grep '
    return jsonify(generales(cad))

@app.route('/chart-data6')
def chartdata6():
    cad='cat /var/log/httpd/access_log | grep "HTTP" | grep "200" | grep '
    return jsonify(generales(cad))

@app.route('/chart-data7')
def chartdataa7():
    return jsonify(chartdata7)



if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True, port=4000)