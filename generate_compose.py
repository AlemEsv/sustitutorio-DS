#!/usr/bin/env python3
"""
Generador simple de docker-compose.yml para microservicios
Versión simplificada y fácil de usar
"""

import yaml
import os


def generate_basic_compose():
    """Genera un docker-compose.yml básico para los 3 microservicios"""
    
    compose_config = {
        'services': {
            'microservicio-A': {
                'build': './microservicio-A',
                'ports': ['8001:8000'],
                'environment': {
                    'SERVICE_NAME': 'microservicio-A',
                    'PORT': '8000'
                }
            },
            'microservicio-B': {
                'build': './microservicio-B',
                'ports': ['8002:8000'],
                'environment': {
                    'SERVICE_NAME': 'microservicio-B',
                    'PORT': '8000'
                }
            },
            'microservicio-C': {
                'build': './microservicio-C',
                'ports': ['8003:8000'],
                'environment': {
                    'SERVICE_NAME': 'microservicio-C',
                    'PORT': '8000'
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
