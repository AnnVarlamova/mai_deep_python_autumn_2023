venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

run:
	./venv/bin/python main.py

test:
	./venv/bin/pytest test_pytest.py
	./venv/bin/python -m unittest test_tic_tac.py

clean:
	rm -rf venv
	rm -rf .pytest_cache
	rm -rf __pycache__

pylint:
	./venv/bin/pylint main.py
.PHONY: venv run test clean pylint
