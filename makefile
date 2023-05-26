#makefile

start:
	poetry run python manage.py runserver 0.0.0.0:8000

install:
	poetry install

build:
	poetry build

lint:
	poetry run flake8 task_manager

translate:
	poetry run django-admin makemessages -l ru

comp_trans:
	poetry run django-admin compilemessages

shell:
	poetry run python manage.py shell

static:
	poetry run python manage.py collectstatic

test:
	poetry run python3 manage.py test ./task_manager/tests/

coverage:
	poetry run coverage run --source='.' manage.py test ./task_manager/tests/