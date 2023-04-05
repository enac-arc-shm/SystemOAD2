from flask import Flask, render_template, redirect, url_for, request
from code_local.system_controller import obtain_mysql_data_cellphones, send_message, system_message, system_delete_cellphone, system_insert_cellphone, obtain_mysql_data_services

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
    return render_template('whatsapp.html', cellphones=cellphones)

@app.route('/test_message/<int:id>')
def test_message(id):
    system_message(id, message=None)
    return redirect(url_for('whatsapp'))


@app.route('/writte_message/<int:id>', methods=['POST'])
def writte_message(id):
    print("Este es el id que recibe", id)
    user_recibe = request.form['user_recibe']
    message = request.form['message']
    system_message(id, message=message)
    return redirect(url_for('whatsapp'))


@app.route('/delete_cellphone/<int:id>')
def delete_cellphone(id):
    system_delete_cellphone(id)
    return redirect(url_for('whatsapp'))

@app.route('/insert_cellphone', methods=['POST'])
def insert_cellphone():
    name = request.form['name']
    number = request.form['number']
    system_insert_cellphone(name, number)
    return redirect(url_for('whatsapp'))

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True, port=4001)