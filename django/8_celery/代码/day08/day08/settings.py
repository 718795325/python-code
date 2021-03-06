"""
Django settings for day08 project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

#setting.py
from celery.schedules import crontab

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5=x4$uhvrvl-#m*fa++b6+@h&+$ww=xtfcysif44-7u8i2f^fj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App.apps.AppConfig',
    'celery',
    'django_celery_results'
]


MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware',#必须是第一个中间件
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware', # 必须是最后一个中间件
]
# CACHE_MIDDLEWARE_SECONDS = 20  #设置超时时间 20秒

ROOT_URLCONF = 'day08.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'day08.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj03',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': '123',
        'PORT': 3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]

# 数据库缓存配置
# CACHES = {
#     'default':{
#         'BACKEND':'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION':'my_cache_table',
#     }
# }

# redis做缓存
CACHES = {
    'default':{
        'BACKEND':'django_redis.cache.RedisCache',#指定缓存类型 redis缓存
        'LOCATION':'redis://@127.0.0.1:6379/1', #缓存地址，@前面是reids的密码，如果没有则去掉
       # 'LOCATION':'redis://127.0.0.1:6379/1', # 没密码
    }
}

# 邮件配置



# celery配置
BROKER_URL='redis://localhost:6379/5'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_SERIALIZER = 'json'              # 任务序列化和反序列化使用json
CELERY_RESULT_SERIALIZER = 'json'            # 结果序列化为json
CELERYD_MAX_TASKS_PER_CHILD = 1000 # 每个worker执行了多少任务就会死掉
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24

# 定时任务
CELERYBEAT_SCHEDULE = {
    # 'schedule-test': {
    #     'task': 'App.tasks.hello_world',
    #     'schedule': timedelta(seconds=10),
    #     'args': (6,)
    # },
"every-ten-second-run-my_task": {
        "task": "App.tasks.do",
        "schedule": crontab(minute="05", hour="16"),
        # "args": (2,)
    }

}


# smtp服务的邮箱服务器
EMAIL_HOST = 'smtp.126.com'
# smtp服务固定的端口是25
EMAIL_PORT = 25

#发送邮件的邮箱
EMAIL_HOST_USER = 'landmark_csl@126.com'
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'INKCXEUXHBFVELTK'
#收件人看到的发件人 <此处要和发送邮件的邮箱相同>
EMAIL_FROM = 'python<landmark_csl@126.com>'



# 日志配置


ADMINS = (
    ('tom', 'landmark_csl@126.com'),
)
# 配置邮件
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = EMAIL_HOST_USER


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
    },
    'filters': {  # 过滤条件
        # 要求debug是False才记录
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'mail_admins': {  # 一旦线上代码报错 邮件提示
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "log", 'debug.log'),  # 文件路径
            'maxBytes': 1024 * 1024 * 5,  # 5兆的数据
            'backupCount': 5,  # 允许有5这样的文件
            'formatter': 'standard',  # 格式
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['debug', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,  # 是否继承父类的log信息
        },
        # 对于不在 ALLOWED_HOSTS 中的请求不发送报错邮件
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}
