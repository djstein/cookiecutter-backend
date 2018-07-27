from .base import *

django_secret_key_response = client.get_secret_value(SecretId='DJANGO_SECRET_KEY')

DJANGO_SECRET_KEY = django_secret_key_response.get('SecretString')

SECRET_KEY = DJANGO_SECRET_KEY if DJANGO_SECRET_KEY else env.str('DJANGO_SECRET_KEY')

# ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')
ALLOWED_HOSTS = ['127.0.0.1', 'x6kb437rh.execute-api.us-east-1.amazonaws.com', ]

# Static Storage Settings
AWS_STORAGE_BUCKET_NAME = '{{cookiecutter.project_slug}}-static'
AWS_S3_CUSTOM_DOMAIN = f's3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}'
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

AWS_AUTO_CREATE_BUCKET = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware'] + MIDDLEWARE  # noqa F405

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
MEDIA_URL = f'https://s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/'

# # Database


# DATABASE_NAME = rds.get('engine') if rds else env.str('POSTGRES_NAME', 'postgres')
# DATABASE_HOST = rds.get('host') if rds else env.str('POSTGRES_HOST', 'localhost')
# DATABASE_PASSWORD = rds.get('password') if rds else env.str('POSTGRES_PASSWORD', '')
# DATABASE_PORT = rds.get('port') if rds else env.int('POSTGRES_PORT', '5432')
# DATABASE_USER = rds.get('username') if rds else env.str('POSTGRES_USER', 'postgres')

# rds_password_key_response = client.get_secret_value(SecretId='{{cookiecutter.rds_secret_key}}')

# RDS_DB_PASSWORD = rds_password_key_response.get('SecretString')

# DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'
# DATABASE_NAME = '{{cookiecutter.db_name}}'
# DATABASE_HOST = '{{cookiecutter.db_host}}'
# DATABASE_PASSWORD = RDS_DB_PASSWORD
# DATABASE_PORT = '{{cookiecutter.db_port}}'
# DATABASE_USER = '{{cookiecutter.db_user}}'


# DATABASES = {
#     'default': {
#         'ENGINE': DATABASE_ENGINE,
#         'NAME': DATABASE_NAME,
#         'USER': DATABASE_USER,
#         'PASSWORD': DATABASE_PASSWORD,
#         'HOST': DATABASE_HOST,
#         'PORT': DATABASE_PORT
#     }
# }
