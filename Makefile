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
	test lint

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml