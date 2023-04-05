# Aquí utilizará la librería pyyaml para generar el archivo de Docker Compose de forma dinámica.
import yaml
import os

# recibe como parámetros la dirección de subred, el primer y último valor del rango de direcciones IP ("range_start" y "range_end")
def generate_dhcp_compose(subnet, range_start, range_end):
    compose_data = {
        "version": "3",
        "services": {
            "dhcp": {
                "image": "networkboot/dhcpd",
                "network_mode": "host",
                "volumes": [
                    "/etc/dhcp:/data"
                ],
                "environment": [
                    f"SUBNET={subnet}",
                    f"RANGE_START={range_start}",
                    f"RANGE_END={range_end}"
                ]
            }
        }
    }

    with open("docker-compose.yml", "w") as compose_file:
        yaml.dump(compose_data, compose_file)
# levantar el servicio DHCP
    os.system("docker-compose up -d")