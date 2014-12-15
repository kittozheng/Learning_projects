Tango With Dajngo 
===

A Simple Practice about Django Web Development

## Requirements

* virturalenv
* Django 1.7
* MySQL
* django-registration-redux 1.1
* Pillow 2.6.1
* wsgiref 0.1.2

## Steps
1. Install virtualenvwrapper and set up a virtualenv using cmd ‘mkvirtualenv tango’
2. Install all packages using the cmd 'pip install -r requirements.pip'
3. Create database using the cmd 'create databases rango default character set utf8 collate utf8_general_ci'
4. Configure your ‘setting.py‘，like database configuration
5. Create tables with cmd ’python manage.py syncdb‘ and create superuser for administration
6. Load test data with cmd 'python populate_rango.py' in virtualenv
7. Run the project with cmd ’python manage.py runserver 0.0.0.0:8089‘  

