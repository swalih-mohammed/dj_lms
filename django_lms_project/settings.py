
from dotenv import load_dotenv
import os
from pathlib import Path
import json


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-&q&&2wsah+6)hh=-)y@++%)=z&pu%gpt&ukou^2a76wpr9n-^1'
SECRET_KEY = os.environ.get('SECRET_KEY')
# print(SECRET_KEY)
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = str(os.environ.get('DEBUG')) == "1"
PRODUCTION = str(os.environ.get('PRODUCTION')) == "1"

print(DEBUG, PRODUCTION)
ALLOWED_HOSTS = ['*']
# if not DEBUG:
#     ALLOWED_HOSTS += [os.environ.get('ALLOWED_HOSTS')]

CORS_ORIGIN_ALLOW_ALL = True


SITE_ID = 1
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'dbbackup',  # django-dbbackup
    'storages',
    'corsheaders',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth',
    'rest_auth.registration',
    'rest_framework',
    'rest_framework.authtoken',
    'users',
    'courses',
    'lessons',
    'quizzes',
    'assets',
    'conversations',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_lms_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'build')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'django_lms_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


if PRODUCTION:
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DB_ENGINE'),
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),

        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'build/static')]
# STATIC_ROOT = "/home/myusername/myproject/stati
STATIC_ROOT = os.path.join(BASE_DIR, "static")


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_COOKIE_NAME = "csrftoken"


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

# ACCOUNT_USERNAME_REQUIRED = True
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_EMAIL_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = 'username'
# ACCOUNT_EMAIL_VERIFICATION = 'none'
# AUTH_USER_MODEL = 'users.User'

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'users.serializers.UserSerializer',
    'TOKEN_SERIALIZER': 'users.serializers.TokenSerializer'
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'users.serializers.CustomRegisterSerializer',
}

DBBACKUP_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DBBACKUP_STORAGE_OPTIONS = {
    'access_key': os.environ.get('AWS_S3_ACCESS_KEY_ID'),
    'secret_key': os.environ.get('AWS_S3_SECRET_ACCESS_KEY'),
    'bucket_name': os.environ.get('AWS_STORAGE_BUCKET_NAME'),
    'default_acl': None
}


AWS_POLLY_ACCESS = os.environ.get('ACCESS_KEY_ID')
AWS_POLLY_SECRET = os.environ.get('POLLY_SECRET_ACCESS_KEY')

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
DEFAULT_FILE_STORAGE = os.environ.get('DEFAULT_FILE_STORAGE')
AWS_S3_ACCESS_KEY_ID = os.environ.get('AWS_S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = os.environ.get('AWS_S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = False

# print(AWS_STORAGE_BUCKET_NAME)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/file.json"


# GOOGLE_APPLICATION_CREDENTIALS = os.environ.get(
#     'GOOGLE_APPLICATION_CREDENTIALS')

# env_path = os.path.join(BASE_DIR, '.env')
# load_dotenv(dotenv_path=env_path)


# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/filename.json'


# This could be any path that the application has read/write permission to

GCS_CREDENTIALS_FILE_PATH = os.path.join(
    BASE_DIR, 'gcs_credentials_file.json')
# print("test")

# test = r'/filename.json

# with open(GCS_CREDENTIALS_FILE_PATH, 'r') as source:
#     # info = json.load(source)
#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = json.load(source)


# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = info


# print(GCS_CREDENTIALS_FILE_PATH)
# f.write(os.getenv('GCS_CREDENTIALS'))

# print("path", GCS_CREDENTIALS_FILE_PATH)
# print(os.environ.get('GCS_CREDENTIALS'))
# {
#     "type":  os.environ.get('type'),
#     "project_id": os.environ.get('project_id'),
#     "private_key_id": os.environ.get('private_key_id'),
#     "private_key": os.environ.get('private_key'),
#     "client_email": os.environ.get('client_email'),
#     "client_id": os.environ.get('client_id'),
#     "auth_uri": os.environ.get('auth_uri'),
#     "token_uri": os.environ.get('token_uri'),
#     "auth_provider_x509_cert_url": os.environ.get('auth_provider_x509_cert_url'),
#     "client_x509_cert_url": os.environ.get('client_x509_cert_url')
# }
