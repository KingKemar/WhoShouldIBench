run-dev:  ## migrations & runserver sur port 2222
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver 0.0.0.0:2222

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
