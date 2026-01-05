.PHONY: setup build up down test-api test-web

setup:
	python3 -m venv venv
	./venv/bin/pip install -r apps/api/requirements.txt
	cd apps/web && npm install

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

test-api:
	docker-compose exec api pytest

test-web:
	docker-compose exec web npm test
