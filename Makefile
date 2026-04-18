SHELL := /bin/bash

ROOT := $(abspath $(CURDIR))
PYTHON ?= python3
harness ?= all

.PHONY: install uninstall

install uninstall:
	@ROOT="$(ROOT)" PYTHON_BIN="$(PYTHON)" "$(ROOT)/scripts/install-loom.sh" "$@" "$(harness)"
