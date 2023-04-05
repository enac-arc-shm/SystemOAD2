import subprocess

output = subprocess.check_output(['systemctl', 'list-units', '--type=service', '--state=running'])

for line in output.splitlines():
    print(line)
