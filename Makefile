# Makefile for TIA Portal Openness Documentation

.PHONY: help clean html pdf test test-content test-links test-build

help:
	@echo "Available commands:"
	@echo "  make html      - Build HTML documentation"
	@echo "  make pdf       - Build PDF documentation"
	@echo "  make clean     - Remove build artifacts"
	@echo "  make test      - Run all tests"
	@echo "  make test-build    - Run build tests"
	@echo "  make test-content  - Run content tests"
	@echo "  make test-links    - Run link tests"
	@echo "  make test-examples - Run example tests"

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

test: test-build test-content test-links test-examples
	@echo ""
	@echo "All tests completed."

test-build:
	@echo "Running build tests..."
	python tests/test_build.py

test-content:
	@echo "Running content tests..."
	python tests/test_content.py

test-links:
	@echo "Running link tests..."
	python tests/test_links.py

test-examples:
	@echo "Running example tests..."
	python tests/test_examples.py

watch:
	@sphinx-autobuild docs/ _build/html/

serve:
	@python -m http.server 8000 --directory _build/html
