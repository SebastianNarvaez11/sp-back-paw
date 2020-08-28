import hashlib
import random
from django.conf import settings
from django.core.management import call_command

def get_guid():
    return hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()

def migrate_all(commit=False):
    for app in settings.INSTALLED_APPS:
        print('migrating', app)
        call_command('makemigrations', app.split('.')[-1:][0])