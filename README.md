# mgnu.org(Amazing Project)
===

MarmaraGNU web sitesi / MarmaraGNU website

Bu repo sadece bir yansımadır. Pull Request'ler [buradan](http://git.mgnu.org/mgnu/website) kabul edilecektir.

This repo is only a MIRROR. Pull Requests will be accepted [here](http://git.mgnu.org/mgnu/website).


===
# Türkçe
===

## SİSTEM GEREKSİNİMLERİ

* python-pip paket yöneticisini yükleyin: ``sudo apt-get install python-pip``
* [isteğe bağlı] Bu projeye katkıda bulunmak için mgnu/website repo'sunu fork'layabilirsiniz.
* Projeyi yerelinize indirin: ``git clone git@github.com:mgnu/website.git``
* Proje ana dizinine gidin
* Paket yöneticisi ile bağımlılıkları yükleyin: ``sudo pip install -r requirements.txt``
* Yerelinize indirdiğiniz projenin ana dizininde ``local_settings.py`` dosyasını oluşturun.

``local_settings.py`` dosyasının içine aşağıdakileri kopyalayın:

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

* Veritabanı için migration'ları oluşturun: ``./manage.py makemigrations``
* Oluşturduğunuz migration'ları çalıştırın: ``./manage.py migrate``
* Veritabanını senkronize edin: ``./manage.py syncdb`` (Aslında bu komut makemigrations ile migrate'i çalıştırır ama ilk kurulumda superuser hesabı oluşturmak isteyip istemediğinizi sorar)
* Projeninizi yerelde çalıştırın: ``./manage.py runserver``

Şimdi tarayıcınızdan [http://127.0.0.1:8000](http://127.0.0.1:8000) adresini açın ve geliştirmeye başlayın.

## Yayınlama (@Yapılacak)

### Otomatik

* Şu anki ``fabfile/project_conf.py`` dosyası, projeyi Amazon'da yayınlamak için konfigüre edilmiştir. Kendi ihtiyacınıza göre bu dosyayı düzenleyin. Django projelerini yayınlama için farklı ortamlarda birçok fab dosyası bulunmaktadır. *fabfile* hakkında detaylı bilgi almak için: [FabFile Dökümantasyonu](http://www.fabfile.org/)

### Basit Kurulum

* Apache veya nginx web sunucusunu kurun
* Projenizi gunicorn'da çalıştırın: ``gunicorn mgnu.wsgi:application``
* Web sunucunuzdan gunicorn portuna ProxyPass yapın.

Apache konfigürasyonu hakkında [detaylı bilgi](http://httpd.apache.org/docs/)

nginx konfigürasyonu hakkında [detaylı bilgi](http://nginx.org/en/docs/)


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

Now open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser and start developing.

## Deployment (@TODO)

### Automatic

* Fill ``fabfile/project_conf.py`` file, currently fabfile is for Amazon deployment, it can be changed due to your needs. There is a lot fab files for django deployment in different environments. More information about [fabfile](http://www.fabfile.org/).

### Basic

* Install nginx or apache
* Run project in gunicorn: ``gunicorn mgnu.wsgi:application``
* Make proxypass to gunicorn port

More information about [Apache configuration](http://httpd.apache.org/docs/)

More information about [nginx configuration](http://nginx.org/en/docs/)
