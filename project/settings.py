import os
from environs import Env

env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': env.str("DB_ENGINE", None),
        'HOST': env.str("DB_HOST", None),
        'PORT': env.str("DB_PORT", None),
        'NAME': env.str("DB_NAME", None),
        'USER': env.str("DB_USER", None),
        'PASSWORD': env.str("DB_PASSWORD", None),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str("SECRET_KEY", None)

DEBUG = env.bool("DEBUG", False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", None)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
