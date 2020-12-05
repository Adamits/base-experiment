.PHONY: linter process_data clean_processed_data

data/processed/:
	@echo "Preprocessing data sets"
	bash data/scripts/build_data_sets.sh

process_data: data/processed/

clean_processed_data:
	rm -rf data/processed/

linter:
	@echo "Linting..."
	@flake8
