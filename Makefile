# Makefile for TIA Portal Openness Documentation

.PHONY: help clean html pdf

help:
	@echo "Available commands:"
	@echo "  make html  - Build HTML documentation"
	@echo "  make pdf   - Build PDF documentation"
	@echo "  make clean - Remove build artifacts"

html:
	python -m sphinx -b html docs/ _build/html/
	@echo ""
	@echo "Build complete. Open _build/html/index.html in your browser."

pdf:
	python -m sphinx -b latex docs/ _build/latex/
	@cd _build/latex/ && make
	@echo ""
	@echo "PDF build complete. Check _build/latex/*.pdf"

clean:
	rm -rf _build/
	rm -rf docs/_build/
	rm -rf docs/_static/
	rm -rf docs/_sources/
	@echo "Cleaned build artifacts."

