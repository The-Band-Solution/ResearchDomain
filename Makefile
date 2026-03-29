.PHONY: install-docs run build-docs

install-docs:
	python -m pip install -e ".[docs]"

run:
	python -m mkdocs serve

build-docs:
	python -m mkdocs build --strict
