all:
	python -m build

init:
	pip install .[dev]

test:
	pytest

clean:
	rm -rf dist build dotdotdot.egg-info htmlcov
