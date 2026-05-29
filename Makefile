.PHONY: help setup lint format type test run docker-build docker-up docker-down clean nuke

help:
	@echo 'make needs an argument, refer to the Makefile for possible commands'

setup:
	@uv sync --all-groups
	@uv run pre-commit install

lint:
	@uv run ruff check .

format:
	@uv run ruff format .

test:
	@uv run pytest

type:
	@uv run mypy src/

run:
	@uv run uvicorn edf.api.main:app --reload

docker-build:
	@docker build -t edf-api .

docker-up:
	@docker compose up -d

docker-down:
	@docker compose down

clean:
	@rm -rf .venv dist __pycache__ .mypy_cache .ruff_cache .pytest_cache
	@docker system prune -f

nuke:
	@rm -rf .venv dist __pycache__ .mypy_cache .ruff_cache .pytest_cache data/processed models/ reports/
	@docker system prune -af
