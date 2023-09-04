runserver:
	python manage.py runserver

migrate:
	python manage.py migrate

startapp:
	python manage.py startapp $(app)

migrations:
	python manage.py makemigrations

superuser:
	python manage.py createsuperuser