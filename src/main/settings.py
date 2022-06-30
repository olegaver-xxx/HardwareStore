import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-)h+ta6ay9i58cet%ie4p5ny(f%p$kr)f6osrbe5so35!+8_4uq'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.store'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'store_db'),
        'USER': os.getenv('POSTGRES_USER', 'admin'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'admin'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redis
REDIS_HOST = os.getenv('REDIS_HOST') or 'localhost'
REDIS_PORT = 6379

# Celery
CELERY_BROKER_HOST = REDIS_HOST
CELERY_BROKER_PORT = REDIS_PORT
# CELERY_SEND_EVENTS = True
# CELERY_ACKS_LATE = True
CELERY_BROKER_HEARTBEAT = 0
# example: 'amqp://myuser:mypassword@localhost:5672'
CELERY_BROKER_URL = f"redis://{REDIS_HOST}:6379/0"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:6379/0"
# CELERY_RESULT_BACKEND = ''
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_WORKER_PREFETCH_MULTIPLIER = 1
CELERY_WORKER_CONCURRENCY = 1
# queues
# CELERY_QUEUES = (
    # Queue('high', Exchange('high'), routing_key='high'),
# )


# scheduler
from celery.schedules import crontab
CELERY_BEAT_SCHEDULE = {
    # http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
    # 'check-idle-1h': {
    #     'task': 'periodic.task2',
    #     'schedule': crontab(hour='*', minute=0)
    # },
    'add-every-1-min': {
        'task': 'main.tasks.test_task',
        'schedule': crontab(),
          # or
          # 'schedule': crontab(minute='*/1', hour='*'),
          # # or
          # 'schedule': 60.0,
        'args': []
    },
    # 'add-every-day': {
    #     'task': 'core.tasks.task_number4',
    #     'schedule': crontab(minute=0, hour=0),
    #     'args': []
    # },
    # },
    # 'backup': {
    #     # start every day
    #     'task': 'myapp.tasks.backup_site',
    #     # 'schedule': crontab(minute='*/20'),   # for tests
    #     'schedule': crontab(minute=0, hour=0),
    # },
}