# Makefile for TIA Portal Openness Documentation

.PHONY: html clean

html:
	python -m sphinx -b html docs/ _build/html/
	@echo ""
	@echo "Build complete. Open _build/html/index.html in your browser."

clean:
	rm -rf _build/
	rm -rf docs/_build/
	@echo "Cleaned build artifacts."
