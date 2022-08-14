#variables
dependencies := install format lint test
pip := python -m pip
lint_files:= hello.py
lint_dirs:= name_lib

#steps
install:
	$(pip) install --upgrade pip &&\
	$(pip) install -r requirements.txt

format:
	black .

lint:
	pylint $(lint_files) $(lint_dirs)

test:
	pytest 

all: $(dependencies)