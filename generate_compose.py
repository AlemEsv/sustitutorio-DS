import yaml

def generate_basic_compose():
    """Genera un docker-compose.yml básico para los 3 microservicios"""

    compose_config = {
        'services': {
            'microservicio-a': {
                'build': './microservicio-a',
                'ports': ['8001:8000'],
                'environment': {
                    'SERVICE_NAME': 'microservicio-a',
                    'PORT': '8000',
                    'profiles': '["debug", "release"]'
                }
            },
            'microservicio-b': {
                'build': './microservicio-b',
                'ports': ['8002:8000'],
                'environment': {
                    'SERVICE_NAME': 'microservicio-b',
                    'PORT': '8000',
                    'profiles': '["debug", "release"]'
                }
            },
            'microservicio-c': {
                'build': './microservicio-c',
                'ports': ['8003:8000'],
                'environment': {
                    'SERVICE_NAME': 'microservicio-c',
                    'PORT': '8000',
                    'profiles': '["debug", "release"]'
                }
            }
        }
    }

    return compose_config


def save_compose_file(config, filename):
    """Guarda la configuración en un archivo YML"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            yaml.dump(config, file, default_flow_style=False, sort_keys=False)
        print(f"Archivo {filename} generado exitosamente")
        return True
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        return False


def main():
    # Generar configuración
    config = generate_basic_compose()
    save_compose_file(config, 'docker-compose.yml')


if __name__ == "__main__":
    main()
