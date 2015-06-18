# -*- coding: utf-8 -*-
from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'taskbuster_db',
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
    }
}

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)
