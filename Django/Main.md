  Install steps
Install Django
````
pip install django
````
Create a new project 
```` 
django-admin startproject RunOrg
````
Run the server 
````
python manage.py runserver
=> http://127.0.0.1:8000/
````


Create a new app
````
python manage.py startapp <appname>
````

Upgrade the database model

````
python manage.py makemigrations
python manage.py migrate
````

In order to view the SQL that a migration will use, execute this in CLI
````
python manage.py sqlmigrate <appname> <migration id>
````

Install crispy forms
````
pip install django-cripsy-forms
````

Django


