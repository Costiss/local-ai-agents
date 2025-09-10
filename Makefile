dev:
	@echo "Running development server..."
	@uv run fastapi dev main.py

format:
	@echo "Formatting code..."
	@uv run ruff format

lint:
	@echo "Linting code..."
	@uv run ruff check --fix
	@uv run basedpyright

check:
	@$(MAKE) format
	@$(MAKE) lint
