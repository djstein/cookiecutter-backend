from .base import *

get_secret_value_response = client.get_secret_value(SecretId='DJANGO_SECRET_KEY')

DEBUG = True

DJANGO_SECRET_KEY = get_secret_value_response.get('SecretString')

SECRET_KEY = DJANGO_SECRET_KEY if DJANGO_SECRET_KEY else env.str('DJANGO_SECRET_KEY')

STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CORS_ORIGIN_WHITELIST = (
    'localhost',
)

# ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default='ip_address')
ALLOWED_HOSTS = ['*', ]

# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# rds = json.dumps(client.get_secret_value("prod/pincer-backend/Database")['SecretString'])

rds = None
DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'
DATABASE_NAME = rds.get('engine') if rds else env.str('POSTGRES_NAME', 'postgres')
DATABASE_HOST = rds.get('host') if rds else env.str('POSTGRES_HOST', 'localhost')
DATABASE_PASSWORD = rds.get('password') if rds else env.str('POSTGRES_PASSWORD', '')
DATABASE_PORT = rds.get('port') if rds else env.int('POSTGRES_PORT', '5432')
DATABASE_USER = rds.get('username') if rds else env.str('POSTGRES_USER', 'postgres')

# DATABASE_NAME = 'PincerDatabase'
# DATABASE_HOST = 'pm1uipw2idtu9yp.ccj2uoxlwo6b.us-east-1.rds.amazonaws.com'
# DATABASE_PASSWORD = 'pincerdatabase'
# DATABASE_PORT = '5432'
# DATABASE_USER = 'pincer'


DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT
    }
}
