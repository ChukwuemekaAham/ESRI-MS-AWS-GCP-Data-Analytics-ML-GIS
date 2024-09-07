.PHONY: format test unit-test integration-test

# Format the code using black
format:
	black .

# Run all tests
test: unit-test integration-test

# Run unit tests
unit-test:
	python -m unittest discover -s unit-and-integration-test -p "test_model.py"

# Run integration tests
integration-test:
	python -m unittest discover -s unit-and-integration-test -p "test_app.py"

# Install pre-commit hooks
pre-commit:
	pre-commit install
