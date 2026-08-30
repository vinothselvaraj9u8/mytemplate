.PHONY: install test test-unit test-ui lint security coverage reports clean all

REPORTS_DIR := reports

install:
	pip install -r requirements.txt

test-unit:
	mkdir -p $(REPORTS_DIR)
	python -m pytest tests/test_main.py --junitxml=$(REPORTS_DIR)/junit-unit.xml -v

test-ui:
	mkdir -p $(REPORTS_DIR)
	python -m pytest tests/test_ui.py --junitxml=$(REPORTS_DIR)/junit-ui.xml -v

test:
	mkdir -p $(REPORTS_DIR)
	python -m pytest tests/ --junitxml=$(REPORTS_DIR)/junit.xml -v

coverage:
	mkdir -p $(REPORTS_DIR)/coverage
	python -m pytest tests/test_main.py \
		--cov=appname \
		--cov-report=xml:$(REPORTS_DIR)/coverage/coverage.xml \
		--cov-report=html:$(REPORTS_DIR)/coverage/html \
		--cov-report=term-missing

lint:
	mkdir -p $(REPORTS_DIR)
	python -m ruff check appname/ --output-format=json --output-file=$(REPORTS_DIR)/ruff-report.json || true
	python -m ruff check appname/

security:
	mkdir -p $(REPORTS_DIR)
	python -m bandit -r appname/ -f json -o $(REPORTS_DIR)/bandit-report.json || true
	python -m bandit -r appname/

reports: test coverage lint security
	@echo "All reports generated in $(REPORTS_DIR)/"

clean:
	rm -rf $(REPORTS_DIR) .pytest_cache .coverage

all: install reports
