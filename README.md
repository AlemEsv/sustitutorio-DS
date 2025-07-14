# Nombre del Proyecto

## Índice

- [Descripción](#descripción)
- [Microservicios A,B y C](#microservicios)
- [Instalación](#instalación-offline)
- [Cómo Ejecutar](#ejecutar-código)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Pruebas](#codigo)


## Descripción

Este proyecto usa patrones de diseño como

- **MEDIATOR**: centralizar coordinación de 3 microservicios

- **FACADE**: orquestar aplicación mediante un makefile

- **BUILDER**: genera dinamicamente el archivo docker-compose.yml mediante un archivo de python

## Microservicios

**A** define un "/process" que recibe informacion y la procesa para mandarla a **B**
**B** aplica una transformacion a los datos recibidos de **A** y le asigna un inventario a un usuario
**C** recibe datos de **B** y los guarda/obtiene mantiene etc

## Instalación offline

Primero clonamos el repositorio de github para obtener todos los archivos:

```bash
git clone https://github.com/AlemEsv/sustitutorio-DS.git
cd susti_DS
```

Ahora instalamos todas las dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar código

Se tiene un makefile que ejecuta los linters necesarios(flake8 y shellcheck) para verificar la correcta sintaxis de código para los microservicios, da formato a cada script en python con black, ejecuta pytest para verificar la integridad de las pruebas smoke, E2E e integración, y por último genera un reporte de cobertura general.

```bash
# ejecuta linters
make lint
# formato
make format
# ejecuta test con pytest
make test
# Genera un reporte HTML con las pruebas
make coverage
# Limpia el estado
make clean
```

## Estructura del Proyecto

```bash
proyecto/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── deploy.yml
├── microservicio-A/
│   ├── archivos
│   └── tests/unit-tests
├── microservicio-B/
│   ├── archivos
│   └── tests/unit-tests
├── microservicio-C/
│   ├── archivos
│   └── tests/unit-tests
├── tests/
│   ├── contract/
│   ├── e2e/
│   ├── smoke/
│   └── integration/
├── docker-compose.yml
├── generate_compose.py
├── README.md
└── .gitignore
```

## Scripts

- **script/compose_builder**

    Script que genera mediante un json un archivo docker-compose para levantar las imagenes que utilizan cada uno de los microservicios (A, B y C).
    Luego lo convierte en formato yml y copia el archivo en el directorio establecido.
