.PHONY: frontend-init
frontend-init:  ## Init
	@cd ${FRONTEND_DIR}; \
	yarn 

.PHONY: frontend-build
frontend-build:  ## Build
	@cd ${FRONTEND_DIR}; \
	yarn build

.PHONY: frontend-start
frontend-start:  ## Start
	@cd ${FRONTEND_DIR}; \
	yarn dev

frontend-test:  ## Run tests
	@cd ${FRONTEND_DIR}; \
	yarn test


