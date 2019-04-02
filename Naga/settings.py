"""
Django settings for Naga project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#&w#0eb@&w^((tox9%)rdp(*z22+p(jzw#z%gw^m6$^a2nr*ts'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'blog',
    'users',
    'ckeditor',
    'ckeditor_uploader',
    'haystack',
]
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),

}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'Naga.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Naga.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# 后台路径设置
NAGA_ADMIN_PATH = "admin"

# 网站路径
NAGA_WEB_URL = 'http://192.168.228.129:8000'




# 富文本编辑器设置
CKEDITOR_UPLOAD_PATH = 'ckeditor_images'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': (
            ['div', 'Source', '-', 'Preview', '-', 'Templates'], 
            ['Cut', 'Copy', 'Paste',  '-', 'Print', 'Scayt'],
            ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat'], 
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button',  'ImageButton', 'HiddenField'], 
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'], 
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'], 
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'], 
            ['Link',  'Unlink',  'Anchor'], 
            ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize'], 
            ['TextColor', 'BGColor'], 
            ['Maximize', 'ShowBlocks', '-',  'pbckcode',  'CodeSnippet'], 
        ),
        'extraPlugins': ','.join(['codesnippet', 'uploadimage', 'widget', 'lineutils']),
    }
}


# 配置全文搜索
# 指定搜索引擎
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
# 指定如何对搜索结果分页，这里设置为每 10 项结果为一页，默认是 20 项为一页
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5
# 添加此项，当数据库改变时，会自动更新索引，非常方便
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
