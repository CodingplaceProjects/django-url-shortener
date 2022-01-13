# URL Shortener

This is a small URL shortener (no deeplink!). It will search for a key and redirect to the URL which is referenced by this key.


## Requirements
- python 3.7 or higher (f-string is in use)


## Setup & Usage
1. [optional] setup and start a virtualenv
2. install django `pip install django` (the latest version should always work fine here)
3. Migrate the database `python ./app/manage.py migrate`
4. Create a superuser `python ./app/manage.py createsuperuser`
5. runserver `python ./app/manage.py runserver`
6. acces Admin portal `python ./app/manage.py admin`
7. Create your Link & have fun!

**Please Note** You will need to host your application before it's accessable from outside.
