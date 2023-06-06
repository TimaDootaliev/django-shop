dev:
	python3 manage.py runserver --settings core.settings.local_settings
prod:
	python3 manage.py runserver --settings core.settings.prod_settings