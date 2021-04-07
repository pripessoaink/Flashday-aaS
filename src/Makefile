SHELL := /bin/bash

BACKEND_ROOT ?= $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
FRONTEND_ROOT ?= $(BACKEND_ROOT)/_site

PYTHON ?= python3
DJANGO_ADMIN ?= $(BACKEND_ROOT)/manage.py

init:: veryclean requirements.txt isolate
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m pip freeze

execute:: build run

run::
	$(PYTHON) $(DJANGO_ADMIN) runserver

build:: compile
	$(PYTHON) $(DJANGO_ADMIN) makemigrations
	$(PYTHON) $(DJANGO_ADMIN) migrate
	$(PYTHON) $(DJANGO_ADMIN) loaddata auth flashday priscilla-pessoa bruna-beatriz rafaela-lunawi johnny-dayverson
	$(PYTHON) $(DJANGO_ADMIN) default_option Pequeno Médio Grande
	$(PYTHON) $(DJANGO_ADMIN) set_prices P:397 M:597 G:797

compile::
	$(PYTHON) $(DJANGO_ADMIN) collectstatic --noinput

test::
	$(PYTHON) $(DJANGO_ADMIN) test

clean::
	rm -fr static
	$(PYTHON) $(DJANGO_ADMIN) reset_migrations _site flashday
	rm -fr db.sqlite3

veryclean:: clean
	find -iname "*.pyc" -iname "*.pyo" -delete


.PHONY: init execute run build compile test clean veryclean