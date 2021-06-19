# Use a standard bash shell, avoid zsh or fish
SHELL:=/bin/bash

ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
BACKEND_DIR:=$(ROOT_DIR)/backend
FRONTEND_DIR:=$(ROOT_DIR)/frontend

.DEFAULT_GOAL := help

.PHONY: help
help:  ## Print this help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort


include backend/local/local.mk