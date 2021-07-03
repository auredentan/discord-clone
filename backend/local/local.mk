.PHONY: backend-clean
backend-clean:  ## Cleanup
	@cd ${BACKEND_DIR}; \
	find . -type d -name "__pycache__" | xargs rm -rf {}; \
	rm -rf .coverage .mypy_cache

.PHONY: backend-init
backend-init: clean  ## Init
	@cd ${BACKEND_DIR}; \
	if [ -z $(POETRY) ]; then echo "Poetry could not be found. See https://python-poetry.org/docs/"; exit 2; fi; \
	poetry install; \
	poetry run pre-commit install 

.PHONY: backend-start
backend-start: backend-start-db backend-start-redis ## Start the dev server
	@cd ${BACKEND_DIR}; \
	poetry run gunicorn src.entrypoints.api:app -w 2 -k uvicorn.workers.UvicornWorker --reload --bind=localhost:8001

.PHONY: backend-test
backend-test:  ## Run tests
	@cd ${BACKEND_DIR}; \
	poetry run pytest ./tests/

.PHONY: backend-format
backend-format:  ## Format files
	@cd ${BACKEND_DIR}; \
	poetry run black src/ tests/; \
	poetry run isort src/ tests/

.PHONY: backend-lint
backend-lint:  ## Lint
	@cd ${BACKEND_DIR}; \
	poetry run pylint --jobs 0 src/

.PHONY: backend-check
backend-check:  ## Check
	@cd ${BACKEND_DIR}; \
	poetry run mypy --config=${BACKEND_DIR}/setup.cfg src/

.PHONY: backend-start-redis
backend-start-redis:
	docker-compose -f ${BACKEND_DIR}/local/docker-compose.yaml up -d redis

.PHONY: backend-start-db
backend-start-db:
	docker-compose -f ${BACKEND_DIR}/local/docker-compose.yaml up -d db