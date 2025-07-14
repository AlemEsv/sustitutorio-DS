# Nombre del Proyecto

## Índice

- [Descripción](#descripcion)
- [Microservicios A,B y C](#microservicios)
- [Instalación](#instalación)
- [Cómo Ejecutar](#ejecutar-código)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Testing](#pruebas)


## Descripción

Este proyecto usa patrones de diseño como

- **MEDIATOR**: centralizar coordinación de 3 microservicios

- **FACADE**: orquestar aplicación mediante un makefile

- **BUILDER**: genera dinamicamente el archivo docker-compose.yml mediante un archivo de python

## Microservicios

**A** define un "/process" que recibe informacion y la procesa para mandarla a **B**
**B** aplica una transformacion a los datos recibidos de **A** y le asigna un inventario a un usuario
**C** recibe datos de **B** y los guarda/obtiene mantiene etc

"script/compose_builder"

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

```bash
# verificar que 
make lint
```

## Estructura del Proyecto

```bash
proyecto/
├── tests/
│   ├── unit/
│   └── integration/
├── README.md
└── .gitignore
```

## Pruebas

```bash
# Ejecutar pruebas
pytest tests/
behave tests/integration/
```

### Cobertura de Código

```bash
# Generar reporte de cobertura
pytest --cov=src
```
