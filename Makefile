.PHONY: help init lint test

help:
	@echo AVAILABLE COMMANDS
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-23s\033[0m%s\n", $$1, $$2}'

init: ## Initialise repo for local development
	@poetry install --sync --with dev
	@poetry run pre-commit install --install-hooks

lint: ## Lint files
	poetry run pre-commit run ruff

test: ## Run tests
	@poetry run pytest
