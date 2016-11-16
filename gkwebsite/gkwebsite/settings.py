# encoding=utf-8
"""
Django settings for gkwebsite project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd&c$@l2*f$d7e^h@vnxgtkj*v*cmg&mff^nw2xt)!i7c!y-#vg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# by dqn14 Nov 13, 2016
# These people will get a e-mail notice when an error occurs.
SERVER_EMAIL = 'site@daydayup.com'
ADMINS = [('Qingnan Duan', 'dqn14@mails.tsinghua.edu.cn'), ('Yunren Bai', '360559261@qq.com'), ('Haoyang Li', 'lihy45@163.com'), ('Yufan Hou', 'evan9669@126.com'), ('Yunqiu Shao', 'shaoyunqiu@163.com')]
#MANAGERS = [('Qingnan Duan', 'dqn14@mails.tsinghua.edu.cn'), ('Yunren Bai', '360559261@qq.com'), ('Haoyang Li', 'lihy45@163.com'), ('Yufan Hou', 'evan9669@126.com'), ('Yunqiu Shao', 'shaoyunqiu@163.com')]

ALLOWED_HOSTS = ['gaokao.northeurope.cloudapp.azure.com', 'localhost', '127.0.0.1', '[::1]']

# by dqn14 Nov 13, 2016
# Default setting
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'

# by dqn14 Nov 13, 2016
# Set to Monday
FIRST_DAY_OF_WEEK = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 添加login app
    # by byr 161003
    'login',

    'database',

    'student.apps.StudentConfig',

    'teacher',

		'volunteer',

    'wechat',
]

# by dqn14 Nov 13, 2016
MIDDLEWARE = [
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# MIDDLEWARE_CLASSES is deprecated in 1.10
# MIDDLEWARE_CLASSES = []

ROOT_URLCONF = 'gkwebsite.urls'
'''
    session 过期设置
    by byr 161011
'''
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

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

WSGI_APPLICATION = 'gkwebsite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_TZ=True

USE_I18N = False

USE_L10N = True

#APPEND_SLASH = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_files")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "gkwebsite")


