from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

named_conf_template = "named.conf.template"
docker_compose_template = "docker-compose.template.yml"
docker_compose_file = "docker-compose.yml"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate-dns', methods=['POST'])
def generate_dns():
    domain_name = request.form["domain_name"]
    forward_zone = request.form["forward_zone"]
    reverse_zone = request.form["reverse_zone"]

    with open("named.conf.template", "r") as f:
        template = f.read()
        named_conf = template.replace("{{ domain_name }}", domain_name).replace(
            "{{ forward_zone }}", forward_zone).replace("{{ reverse_zone }}", reverse_zone)
    with open("named.conf", "w") as f:
        f.write(named_conf)

    with open("docker-compose.template.yml", "r") as f:
        template = f.read()
        docker_compose = template.replace("{{ domain_name }}", domain_name)
    with open("docker-compose.yml", "w") as f:
        f.write(docker_compose)

    subprocess.run(['docker', 'build', '-t', 'networkboot/bind9:latest', '.'])
    subprocess.run(['docker-compose', '-f', 'docker-compose.yml', 'up', '-d',
                   '--force-recreate'], cwd='.', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return "DNS server started successfully!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
