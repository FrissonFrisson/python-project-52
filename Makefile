.PHONY:	test	lint	test-coverage

install:
	poetry install
	
run:
	poetry run python3 manage.py runserver

test:
	$(MAKE) lint; poetry run python3 manage.py test

makemigrations:
	poetry run python3 manage.py makemigrations

migrate:
	poetry run python3 manage.py migrate

lint:
	poetry run flake8 task_manager

test-coverage:
	coverage run  --source='.' manage.py test task_manager
	coverage report
	coverage lcov -o coverage/lcov.info