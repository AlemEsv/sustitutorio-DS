# errores en formato de archivos python
black . --check
# errores de sintaxis en archivos python
flake8 . --exclude=__pycache__ --max-line-length=120
# errores de sintaxis en archivos bash
shellcheck scripts/ci.sh
# pasar pruebas unitarias
pytest --maxfail=1 --disable-warnings --cov=src
# generar reporte html 
pytest tests/ --cov=microservicio-A --cov=microservicio-B --cov=microservicio-C --cov-report=html --cov-report=term
# guardar 5 ultimos commits en un CHANGELOG.md
git log --oneline -n 5 >> CHANGELOG.md
# despliegue usando docker compose
docker-compose build