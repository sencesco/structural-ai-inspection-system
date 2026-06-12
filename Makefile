.PHONY: api-dev web-dev

api-dev:
	cd apps/api && uvicorn app.main:app --reload

web-dev:
	cd apps/web && npm run dev

