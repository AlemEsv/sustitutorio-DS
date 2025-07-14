.PHONY: lint test report clean

lint:
	scripts/ci.sh

test:
	pytest tests/

report:
	coverage report --fail-under=90

clean:
	echo "limpieza exitosa(falta colocar)"