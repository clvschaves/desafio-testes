install:
	pip install -r requiriments.txt

test:
	pytest -v --html=report.html --self-contained-html --cov=desafio
	coverage html