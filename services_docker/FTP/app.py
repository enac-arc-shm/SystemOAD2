from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

vsftpd_conf_template = "vsftpd.conf.template"
docker_compose_template = "docker-compose.template.yml"
docker_compose_file = "docker-compose.yml"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate-ftp', methods=['POST'])
def generate_ftp():
    ftp_username = request.form["ftp_username"]
    ftp_password = request.form["ftp_password"]
    ftp_domain = request.form["ftp_domain"]

    with open("vsftpd.conf.template", "r") as f:
        template = f.read()
        vsftpd_conf = template.replace("{{ ftp_username }}", ftp_username).replace(
            "{{ ftp_password }}", ftp_password).replace("{{ ftp_domain }}", ftp_domain)
    with open("vsftpd.conf", "w") as f:
        f.write(vsftpd_conf)

    with open("docker-compose.template.yml", "r") as f:
        template = f.read()
        docker_compose = template.replace("{{ ftp_domain }}", ftp_domain)
    with open("docker-compose.yml", "w") as f:
        f.write(docker_compose)

    subprocess.run(['docker', 'build', '-t', 'fauria/vsftpd:latest', '.'])
    subprocess.run(['docker-compose', '-f', 'docker-compose.yml', 'up', '-d',
                   '--force-recreate'], cwd='.', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return "FTP server started successfully!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)