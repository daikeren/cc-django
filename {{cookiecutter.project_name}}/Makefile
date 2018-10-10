TAG=latest

lint:
	flake8 .

up:
	docker-compose up

down:
	docker-compose down

build:
	docker build . -t {{cookiecutter.project_slug}}:$(TAG)

migrate:
	docker-compose run --rm web python3 ./manage.py migrate

shell:
	docker-compose run --rm web python3 ./manage.py shell_plus

django_manage:
	docker-compose run --rm web python3 ./manage.py ${ARGS}
