from .base import *

get_secret_value_response = client.get_secret_value(SecretId='DJANGO_SECRET_KEY')

DEBUG = True

SECRET_KEY = get_secret_value_response.get('SecretString') if aws_env else env.str('DJANGO_SECRET_KEY')

STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CORS_ORIGIN_WHITELIST = (
    'localhost',
)

# ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default='ip_address')
ALLOWED_HOSTS = ['*', ]

# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
