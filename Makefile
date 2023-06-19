# Django Makefile

# Define the Python interpreter
PYTHON_INTERPRETER = python3

# Install project dependencies
install:
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

# Run database migrations
migrate:
	$(PYTHON_INTERPRETER) manage.py migrate

# Create a new Django superuser
createsuperuser:
	$(PYTHON_INTERPRETER) manage.py createsuperuser

# Run development server
runserver:
	$(PYTHON_INTERPRETER) manage.py runserver

# Run tests
test:
	$(PYTHON_INTERPRETER) manage.py test

# Clean up pycache and compiled Python files
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

# Run linting using flake8
lint:
	flake8

# Run code formatting using black
format:
	black .


# Help - List available commands
help:
	@echo "Available commands:"
	@echo "  make install          - Install project dependencies"
	@echo "  make migrate          - Run database migrations"
	@echo "  make createsuperuser  - Create a new Django superuser"
	@echo "  make runserver        - Run development server"
	@echo "  make test             - Run tests"
	@echo "  make generate_secret_key  - Generate a Django secret key"
	@echo "  make clean            - Clean up pycache and compiled Python files"
	@echo "  make lint             - Run linting using flake8"
	@echo "  make format           - Run code formatting using black"
	@echo "  make check            - Run all the checks (linting and tests)"
	@echo "  make help             - Show this help message"

# Set the default make target to show the help message
.DEFAULT_GOAL := help
