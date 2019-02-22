all:
	python setup.py sdist bdist_wheel

init:
	pip install -r requirements.txt

test:
	pytest

clean:
	rm -rf dist build dotdotdot.egg-info htmlcov
