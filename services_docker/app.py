from flask import Flask, request
import gen_dhcp_compose

app = Flask(__name__)

# Cuando se recibe una petición, obtiene los valores de los parámetros "subnet", 
# "range_start" y "range_end" y llama a la función "generate_dhcp_compose" con estos valores

@app.route('/dhcp', methods=['POST'])
def generate_dhcp():
    subnet = request.form['subnet']
    range_start = request.form['range_start']
    range_end = request.form['range_end']
    gen_dhcp_compose(subnet, range_start, range_end)
    return "DHCP service generated successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)