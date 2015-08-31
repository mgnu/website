# mgnu.org
===

MarmaraGNU web sitesi


===
# English
===

## SYSTEM REQUIREMENTS

* Install python-pip: ``sudo apt-get install python-pip``
* [optional] If you want to contribute project, fork github repo and then clone from your own repository
* Clone the project: ``git clone git@github.com:mgnu/website.git``
* Go to project directory
* Install project requirements: ``sudo pip install -r requirements.txt``
* Create ``local_settings.py`` file in project root for local environment.

Copy and add following text to your ``local_settings.py`` file:

```python
from __future__ import unicode_literals
import os
# Custom settings for local environment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
# SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, MEDIA_URL.strip("/"))
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
```

* Make migrations: ``./manage.py makemigrations``
* Migrate: ``./manage.py migrate``
* Syncdb (actually same as migrate but also creates admin user): ``./manage.py syncdb``
* Run local server: ``./manage.py runserver``

Now open http://127.0.0.1:8000 in your browser and start developing.

## Deployment (@TODO)

### Automatic

* Fill ``fabfile/project_conf.py`` file, currently fabfile is for Amazon deployment, it can be changed due to your needs. There is a lot fab files for django deployment in different environments.

### Basic

* Install nginx or apache
* Run project in gunicorn: ``gunicorn mgnu.wsgi:application
* Make proxypass to gunicorn port
