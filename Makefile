make:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

createsuperuser:
	python3 manage.py createsuperuser

runserver:
	python3 manage.py runserver localhost:9007

runserver_production:
	python3 manage.py runserver localhost:9007 --noinput --settings=config.settings.production

create_database:
	sudo -u postgres psql -U postgres -tc """SELECT 1 FROM pg_database WHERE datname = "demo-portifolio"; """ | grep -q 1 || sudo -u postgres psql -U postgres -c """CREATE DATABASE "demo_portifolio";"""

setup:
	pip install poetry
	poetry install --no-root
	python3 manage.py migrate
	python3 manage.py createsuperuser
