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
	uv add PyYAML pytest
	uv run pytest tests/
	
test-coverage:
	uv add PyYAML pytest pytest-cov
	uv run pytest --cov=gendiff --cov-report=xml --cov-branch --junitxml=test-results.xml

selfcheck: check
.PHONY: install gendiff build package-install lint test test-coverage check selfcheck