# Makefile

# Define the Python interpreter
PYTHON = python3

# Define the virtual environment directory
VENV = venv

# Define the source directory
SRC = src

# Define the test directory
TESTS = tests

# Define the documentation directory
DOCS = docs

# Define the build directory
BUILD = build

# Define the distribution directory
DIST = dist

# Define the requirements file
REQUIREMENTS = requirements.txt

# Define the setup file
SETUP = setup.py

# Define the main script
MAIN = main.py

# Define the prompt generator script
PROMPT_GENERATOR = prompt_generator.py

# Define the utility script
UTILS = utils.py

# Define the diffusion model script
DIFFUSION_MODEL = diffusion_model.ipynb

# Define the README file
README = README.md

# Define the dotenv file
DOTENV = .env

# Define the API keys file
API_KEYS = api_keys.py

# Define the clean files
CLEAN_FILES = $(VENV) $(BUILD) $(DIST) *.pyc __pycache__

# Define the clean directories
CLEAN_DIRS = $(CLEAN_FILES) $(DOCS) $(TESTS)

# Default target
all: install test

# Install dependencies
install:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install -r $(REQUIREMENTS)

# Run tests
test:
	$(VENV)/bin/pytest $(TESTS)

# Run the main script
run:
	$(VENV)/bin/python $(SRC)/$(MAIN)

# Run the prompt generator script
run_prompt_generator:
	$(VENV)/bin/python $(SRC)/$(PROMPT_GENERATOR)

# Generate documentation
docs:
	$(VENV)/bin/sphinx-build -b html $(DOCS) $(BUILD)/html

# Build the project
build:
	$(PYTHON) $(SETUP) sdist bdist_wheel

# Clean the build artifacts
clean:
	rm -rf $(CLEAN_DIRS)

# Clean the virtual environment
clean_venv:
	rm -rf $(VENV)

# Clean the build directory
clean_build:
	rm -rf $(BUILD)

# Clean the distribution directory
clean_dist:
	rm -rf $(DIST)

# Clean the test directory
clean_tests:
	rm -rf $(TESTS)

# Clean the documentation directory
clean_docs:
	rm -rf $(DOCS)

# Clean the dotenv file
clean_dotenv:
	rm -f $(DOTENV)

# Clean the API keys file
clean_api_keys:
	rm -f $(API_KEYS)

# Clean the diffusion model file
clean_diffusion_model:
	rm -f $(DIFFUSION_MODEL)

# Clean the README file
clean_readme:
	rm -f $(README)

# Clean the utility script
clean_utils:
	rm -f $(UTILS)

# Clean the main script
clean_main:
	rm -f $(MAIN)

# Clean the prompt generator script
clean_prompt_generator:
	rm -f $(PROMPT_GENERATOR)

# Clean all files and directories
clean_all: clean_venv clean_build clean_dist clean_tests clean_docs clean_dotenv clean_api_keys clean_diffusion_model clean_readme clean_utils clean_main clean_prompt_generator