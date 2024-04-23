install: ## Install the poetry environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry install
	@ poetry run pre-commit install
	@poetry shell

repl: ## Starts the RRPL of Vadi language
	@poetry run python3 -m vadi.repl

check: ## Run code quality tools.
	@echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check"
	@poetry check --lock
	@echo "🚀 Linting code: Running pre-commit"
	@poetry run pre-commit run -a
	@echo "🚀 Static type checking: Running mypy"
	@poetry run mypy
	@echo "🚀 Checking for obsolete dependencies: Running deptry"
	@poetry run deptry .

test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@poetry run pytest --cov --cov-config=pyproject.toml --cov-report=xml

build: clean-build ## Build wheel file using poetry
	@echo "🚀 Creating wheel file"
	@poetry build

clean-build: ## clean build artifacts
	@rm -rf dist

clean: clean-build ## clean build artifacts, dev tools cache
	@rm -rf .ruff_cache .pytest_cache .mypy_cache
	@find . -type d -name "__pycache__" -exec rm -rf {} +


publish: ## publish a release to pypi.
	@echo "🚀 Publishing: Dry run."
	@poetry publish --dry-run
	@echo "🚀 Publishing."
	@poetry publish

build-and-publish: build publish ## Build and publish.

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


.PHONY: install, repl, check, test, build, clean-build, clean, build-and-publish, help

.DEFAULT_GOAL := help

# Suppress Entering/Leaving print output from make
MAKEFLAGS += --no-print-directory
