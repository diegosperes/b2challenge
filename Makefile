benchmark:
	@echo "AVG time to process a range from 0 to 10 billions: $$(python main.py) seconds."

tests:
	@python -m unittest discover . -p 'test*'