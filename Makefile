run:
	poetry run python3 manage.py runserver

test:
	poetry run python3 manage.py test

makemigrations:
	poetry run python3 manage.py makemigrations

migrate:
	poetry run python3 manage.py migrate
