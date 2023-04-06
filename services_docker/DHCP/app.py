from urllib import response
from flask import Flask, render_template, request
import subprocess
import ipaddress 


# app = Flask(__name__)
# docker_compose_file = 'docker-compose.yml'


# @app.route('/')
# def index():
#    return render_template('index.html')


# @app.route('/generate', methods=['GET', 'POST'])
# def generate_dhcp():
#    subnet = request.form["subnet"]
#    gateway = request.form["gateway"]
#    start_ip = request.form["start_ip"]
#    end_ip = request.form["end_ip"]


#    with open("dhcpd.conf.template", "r") as f:
#        template = f.read()
#        dhcpd_conf = template.replace("{{ subnet }}", subnet).replace("{{ gateway }}", gateway).replace("{{ start_ip }}", start_ip).replace("{{ end_ip }}", end_ip)
#    with open("dhcpd.conf", "w") as f:
#        f.write(dhcpd_conf)


#    client = docker.from_env()
#    compose_file = "docker-compose.yml"
#    project_name = "dhcp"
#    result = client.containers.run("docker/compose:1.29.2", f"-f {compose_file} -p {project_name} up -d", remove=True)

#    if "Creating network" in result.decode("utf-8"):
#        return response("Archivo de configuración generado y servicio de DHCP levantado correctamente.", status=200)
#    else:
#        return response("Error al generar el servicio")

#        with open(docker_compose_file, 'w') as f:


#            f.write(f'''
# version: '3'
# services:
#  dhcp:
#    image: networkboot/dhcpd
#    volumes:
#      - ./dhcpd.conf:/etc/dhcp/dhcpd.conf
#    environment:
#      SUBNET: {subnet}
#      RANGE_START: {range_start}
#      RANGE_END: {range_end}
#    restart: always
# ''')
# Ejecutamos el comando de docker-compose up
#            result = subprocess.run(
#               ['docker-compose', '-f', docker_compose_file, 'up', '-d'], stdout=subprocess.PIPE)
#            output = result.stdout.decode('utf-8')
#            return render_template('success.html', output=output)
# return render_template('index.html')

# Levanta el servicio DHCP
# path = '/home/anasnh/Documentos/BIG DATA/docker/app.py'
# command = ['docker-compose', '-f', 'docker-compose.yml', 'up', '-d']
# process = subprocess.Popen(command, cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# error = process.communicate()
# os.system(command)
# if error:
# print(f"Error al ejecutar docker-compose: {error}")
# else:
# print("docker-compose se ha ejecutado correctamente")

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


# @app.route('/generate-dhcp', methods=['POST'])
# def generate_dhcp():
#    subnet = request.form["subnet"]
#    gateway = request.form["gateway"]
#    start_ip = request.form["start_ip"]
#    end_ip = request.form["end_ip"]
#    subnet_mask = request.form["subnet_mask"]

#    with open("dhcpd.conf.template", "r") as f:
#        template = f.read()
#        dhcpd_conf = template.replace("{{ subnet }}", subnet).replace(
#            "{{ gateway }}", gateway).replace("{{ start_ip }}", start_ip).replace("{{ end_ip }}", end_ip).replace("{{ subnet_mask }}", subnet_mask)
#    with open("dhcpd.conf", "w") as f:
#        f.write(dhcpd_conf)

#    with open("docker-compose.template.yml", "r") as f:
#        template = f.read()
#        docker_compose = template.replace("{{ subnet }}", subnet).replace(
#            "{{ gateway }}", gateway).replace("{{ start_ip }}", start_ip).replace("{{ end_ip }}", end_ip).replace("{{ subnet_mask }}", subnet_mask)
#    with open("docker-compose.yml", "w") as f:
#        f.write(docker_compose)

#    subprocess.run(['docker', 'build', '-t', 'networkboot/dhcpd:latest', '.'])
#    subprocess.run(['docker-compose', '-f', 'docker-compose.yml', 'up', '-d',
#                   '--force-recreate'], cwd='.', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    subprocess.run(['docker-compose', '-f', 'docker-compose.yml', '-v', '$(pwd)/data:/data', 'up', '-d', '--force-recreate'])
#    return "DHCP server started successfully!"

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
    app.run(debug=True, host='0.0.0.0', port=5001)
