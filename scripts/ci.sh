# errores en formato de archivos python
black /src --check
# errores de sintaxis en archivos python
flake8 /src #[anotaciones]
# errores de sintaxis en archivos bash
shellcheck scripts/ci.sh
# pasar pruebas unitarias
pytest --maxfail=1 --disable-warnings --cov=src

# generar reporte html 

# guardar 5 ultimos commits en un CHANGELOG.md
git log --pretty=format

# levantar malla en minikube
