isort:
	isort -rc --atomic .

black:
	black .

flake8:
	flake8

lint: isort black flake8
