project := template_python
venv := .venv
bin := $(venv)/bin


# Install dependencies
.PHONY: install i
i: install
install:
	uv venv $(venv)
	uv pip install -e .[dev]

# Run tests
.PHONY: pytest t test
test: pytest
pytest:
	$(bin)/pytest .
t:
	$(bin)/pytest . --no-cov

# Run ruff
.PHONY: ruff ruff-fix ruff-full f fix
ruff:
	$(bin)/ruff check --output-format concise .
ruff-full:
	$(bin)/ruff check .
ruff-fix: fix
f: fix
fix:
	$(bin)/ruff check --fix .

# Run mypy
.PHONY: mypy m
m: mypy
mypy:
	$(bin)/mypy .

# Run all quality assessment checks
.PHONY: quality_assessment qa q
qa: ruff pytest mypy
q: qa
quality_assessment: qa

# Run project
.PHONY: run r
r: run
run:
	$(bin)/python -m $(project)
