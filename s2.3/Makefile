.PHONY: install
install:
	pip install -r ./backend/requirements.txt

.PHONY: run-local
run-local:
	uvicorn main:app --reload

.PHONY: run-prod
run-prod:
	uvicorn main:app --host 0.0.0.0