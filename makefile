.PHONY: install lint format test coverage clean docker-build docker-up docker-down help

# Instalar dependencias
install:
	pip install -r requirements.txt

# Linters para microservicios
lint:
	flake8 microservicio-A microservicio-B microservicio-C --exclude=__pycache__ --max-line-length=110

# Formateo de código con black
format:
	black microservicio-A microservicio-B microservicio-C

# Ejecutar todas las pruebas
test:
	pytest tests/ -v

# Ejecutar pruebas con coverage
coverage:
	pytest tests/ --cov=microservicio-A --cov=microservicio-B --cov=microservicio-C --cov-report=html --cov-report=term

# Limpiar archivos cache generados por las pruebas
clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +

# Show help
help:
	@echo "Available commands:"
	@echo "  install      - Instalar dependencias"
	@echo "  lint         - Ejecutar linters para cada microservicio"
	@echo "  format       - Formatear código con black"
	@echo "  test         - Ejecutar todas las pruebas"
	@echo "  coverage     - Genera un reporte HTML con coverage"
	@echo "  clean        - Limpia el estado del proyecto"