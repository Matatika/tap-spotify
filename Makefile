.PHONY: help init lint lint-fix test

help:
	@echo AVAILABLE COMMANDS
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-23s\033[0m%s\n", $$1, $$2}'

init: ## Initialise repo for local development
	@poetry install -v
	@! test -d ~/.cache/pre-commit || poetry run pre-commit clean
	@poetry run pre-commit install -f --install-hooks

lint: ## Lint source files
	poetry run autoflake --check --recursive --exclude tests --remove-all-unused-imports --remove-duplicate-keys --remove-unused-variables --verbose tap_spotify
	poetry run isort --check --diff tap_spotify
	poetry run black --check --diff tap_spotify
	poetry run flake8 --max-complexity 10 tap_spotify

lint-fix: ## Lint source files and fix any issues
	poetry run autoflake --in-place --recursive --exclude tests --remove-all-unused-imports --remove-duplicate-keys --remove-unused-variables --verbose tap_spotify
	poetry run isort tap_spotify
	poetry run black tap_spotify

test: ## Run tests
	@poetry run pytest
