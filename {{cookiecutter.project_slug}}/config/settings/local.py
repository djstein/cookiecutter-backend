from .base import *

aws_env = json.dumps(secrets.get_secrets_value("prod/{{cookiecutter.project_slug}}/Database")['SecretString'])

DEBUG = True

SECRET_KEY = aws_env.get('DJANGO_SECRET_KEY') if aws_env else env.str('DJANGO_SECRET_KEY')

STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CORS_ORIGIN_WHITELIST = (
    'localhost',
)

# ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default='ip_address')
ALLOWED_HOSTS = ['*', ]

# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
