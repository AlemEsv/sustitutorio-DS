# Nombre del Proyecto

## Índice

- [Descripción](#descripción)
- [Microservicios A,B y C](#microservicios)
- [Instalación](#instalación-offline)
- [Cómo Ejecutar](#ejecutar-código)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Scripts generales](#scripts)
- [Referencias](#referencias)

## Descripción

Este proyecto usa patrones de diseño como

- **MEDIATOR**: centralizar coordinación de 3 microservicios.

- **FACADE**: orquestar aplicación mediante un makefile.

- **BUILDER**: genera dinamicamente el archivo docker-compose.yml mediante un archivo de python.

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
├── scripts/
│   ├── ci.sh
│   └── mesh.py
├── docker-compose.yml
├── generate_compose.py
├── README.md
└── .gitignore
```

## Scripts

- **compose_builder.py**

    Script que genera mediante un json un archivo docker-compose para levantar las imagenes que utilizan cada uno de los microservicios (A, B y C).
    Luego lo convierte en formato yml y copia el archivo en el directorio establecido.

    ```python
    python generate_compose.py
    ```

- **mesh.py**

    Script que realiza llamados al servicio A, gestiona los llamados hacia el servicio B y realiza logging al servicio C mediante requests al servidor cuando se levanta los servicios gracias a docker-compose

    ```python
    python scripts/mesh.py
    ```

- **git_graph**

    Script que genera un DAG de los últimos 5 commits hechos, muestra el commit-hash mediante matplotlib.

    ```python
    python scripts/git_graph.py
    # saldrá una pantalla mostrando los nodos
    ```

- **ci.sh**

    Script con la misma funcionalidad que el job "linters" en workflows/ci.yml, el cual se encarga de verificar que la sintaxis de código en bash y python sea la correcta, cambia el formato a uno más generalizado con black y levanta los servicios de manera local con docker-compose.

    ```python
    python scripts/git_graph.py
    # saldrá una pantalla mostrando los nodos
    ```

## Preguntas teóricas

1. Por qué Git es un DAG

    Git usa gráfos aciclicos para facilitar la vista a diferentes proyectos en base a sus commits, no es posible generar ciclos ya que cada que existen modificaciones en archivos y al ser añadidos al repositorio git, estos cambian su hash, además de esta forma se puede obtener estados anteriores a objetos creados ya que solo se deberá apuntar a un hash de un objeto previo a su modificación.

    Además permite tener múltiples padres, otorgando la estructura de arbol no tan estricta.

    ![dag-de-prueba](images/dag.png)

2. Mediator vs Adapter

Mediator organiza un objeto mediador por el cual todos los servicios deberían "pasar" para realizar las pruebas extremo a extremo o las pruebas smoke, esto conlleva tiempo y recursos, ya que este objeto busca que todo tipo de servicio sea capaz de comunicarse con el otro mediante dicho mediador, esto permite la inyección de lógica a base de dicho objeto creado.
En el caso del método Adapter, este último busca la forma de adaptar todos los servicios, sirve para servicios más simples, da menos problemas .

## Referencias

Código de referencia:

- [https://github.com/AlemEsv/repo-test-susti-1](https://github.com/AlemEsv/repo-test-susti-1)
- [https://python.igraph.org/en/main/tutorials/generate_dag.html](script-generate-dag)
- [https://www.oreilly.com/library/view/git-version-control/9781789137545/12ad80de-2c0d-43b6-8157-b991084640e3.xhtml](git-dag)
- [https://medium.com/@a.kago1988/why-the-git-graph-is-a-directed-acyclic-graph-dag-f9052b95f97f](git-dag-vs-tree)
- [https://refactoring.guru/es/design-patterns](patrones-diseño)