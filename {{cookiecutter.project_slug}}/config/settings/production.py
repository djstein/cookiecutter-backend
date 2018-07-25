from .base import *

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

SECRET_KEY = env.str('DJANGO_SECRET_KEY')

STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

# Static Storage Settings
AWS_STORAGE_BUCKET_NAME = '{{cookiecutter.project_slug}}-static'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_AUTO_CREATE_BUCKET = True
