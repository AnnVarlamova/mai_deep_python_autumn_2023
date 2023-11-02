venv:
	python3 -m venv venv

test:
	./venv/bin/python -m unittest test_d.py
	./venv/bin/python -m unittest test_metacl.py

clean:
	rm -rf venv
	rm -rf __pycache__
	rm -rf .coverage

pylint:
	./venv/bin/pip install -r requirements.txt
	./venv/bin/pylint metacl.py

coverage:
	./venv/bin/pip install -r requirements.txt
	./venv/bin/coverage run -m unittest test_metacl.py
	./venv/bin/coverage report -m

flake8:
	./venv/bin/pip install -r requirements.txt
	./venv/bin/flake8 metacl.py

.PHONY: venv run test clean pylint coverage flake8
