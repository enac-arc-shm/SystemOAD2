from urllib import response
from flask import Flask
from flask import render_template, request
import subprocess
import ipaddress 

app = Flask(__name__)

dhcpd_conf_template = "dhcpd.conf.template"
docker_compose_template = "docker-compose.template.yml"
docker_compose_file = "docker-compose.yml"


def validate_ip_address(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-dhcp', methods=['POST'])
def generate_dhcp():
    subnet = request.form["subnet"]
    gateway = request.form["gateway"]
    start_ip = request.form["start_ip"]
    end_ip = request.form["end_ip"]
    subnet_mask = request.form["subnet_mask"]

    # Validar que las direcciones IP ingresadas sean correctas
    if not validate_ip_address(subnet) or not validate_ip_address(gateway) or not validate_ip_address(start_ip) or not validate_ip_address(end_ip):
        return "Error: Dirección IP inválida"

    with open("dhcpd.conf.template", "r") as f:
        template = f.read()
        dhcpd_conf = template.replace("{{ subnet }}", subnet).replace(
            "{{ gateway }}", gateway).replace("{{ start_ip }}", start_ip).replace("{{ end_ip }}", end_ip).replace("{{ subnet_mask }}", subnet_mask)
    with open("dhcpd.conf", "w") as f:
        f.write(dhcpd_conf)

    with open("docker-compose.template.yml", "r") as f:
        template = f.read()
        docker_compose = template.replace("{{ subnet }}", subnet).replace(
            "{{ gateway }}", gateway).replace("{{ start_ip }}", start_ip).replace("{{ end_ip }}", end_ip).replace("{{ subnet_mask }}", subnet_mask)
    with open("docker-compose.yml", "w") as f:
        f.write(docker_compose)

    subprocess.run(['docker', 'build', '-t', 'networkboot/dhcpd:latest', '.'])
    subprocess.run(['docker-compose', '-f', 'docker-compose.yml', 'up', '-d',
                   '--force-recreate'], cwd='.', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    subprocess.run(['docker-compose', '-f', 'docker-compose.yml', '-v', '$(pwd)/data:/data', 'up', '-d', '--force-recreate'])
    return "DHCP server started successfully!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
