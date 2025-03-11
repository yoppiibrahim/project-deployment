.PHONY: run_builder run_inference install clean check runner_builder runner_inference
.DEFAULT_GOAL:=runner_inference

run_builder: install
	cd src && poetry run python runner_builder.py

run_inference: install
	cd src && poetry run python runner_inference.py

install: pyproject.toml
	poetry install

clean:
	for /d /r %%d in (__pycache__) do rmdir /q /s "%%d"

check :	
	poetry run flake8 src/

runner_builder: check run_builder clean

runner_inference: check run_inference clean