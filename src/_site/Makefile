SHELL := /bin/bash

FRONTEND_ROOT ?= $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
NODE_ROOT ?= $(FRONTEND_ROOT)/node_modules

init:: veryclean $(FRONTEND_ROOT)/package.json
	npm install --prefix $(FRONTEND_ROOT)

execute:: build run ## Build and Run application

run:: ## Launch application locally

build:: ## Process source code into an executable program

compile:: ## Treat file generation
	npm run compile:css --prefix $(FRONTEND_ROOT)

test:: ## Verify application's behavior requirements completeness

clean:: ## Delete all files created through Build process
	rm -fr static/css/

veryclean:: clean ## Delete all generated files
	rm -fr node_modules
	rm -fr package-lock.json


.ONESHELL:
.PHONY: init execute run build compile test clean veryclean
