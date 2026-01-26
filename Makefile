install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check gendiff


check:
	lint test

test:
	uv run pytest tests/
	pip install PyYAML
	pytest --cov=gendiff --cov-report=xml --cov-branch --junitxml=test-results.xml

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml tests/

selfcheck: check
.PHONY:  install dev-install gendiff build package-install lint test test-coverage check selfcheck