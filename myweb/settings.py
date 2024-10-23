"""
Django settings for myweb project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lx9%+ygtkfr@r35dyz)()_dfz&!w@5gri54=qx^&r2i8txk$#u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django.contrib.humanize',  # humanize 필터 활성화
    'users',
    'home',
    'shop',
    'carts',
    'orders',
    'reviews.apps.ReviewsConfig',
    'benefit',
    'cs',
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

ROOT_URLCONF = 'myweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'myweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.CustomUser'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# 정적 파일의 기본 URL 경로 설정
STATIC_URL = '/static/'

# 정적 파일들이 위치하는 디렉토리 경로를 설정
STATICFILES_DIRS = [
     os.path.join(BASE_DIR, 'static'),
]

# 정적 파일이 수집되어 저장될 디렉토리 경로
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 미디어 파일의 기본 URL 경로 설정 (사용자 업로드 파일 등)
MEDIA_URL = '/media/'

# 미디어 파일들이 저장될 디렉토리 경로 설정
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CART_SESSION_ID ='cart'

# Review settings
MAX_REVIEW_LENGTH = 500  # 최대 리뷰 길이
REVIEW_PER_PAGE = 10  # 페이지당 표시될 리뷰 수

# Review image settings
REVIEW_IMAGE_MAX_SIZE = 5 * 1024 * 1024  # 5MB in bytes
REVIEW_IMAGE_ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/gif']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

# 403 에러 핸들러를 커스텀 페이지로 설정
HANDLER403 = 'your_project.views.custom_permission_denied_view'


# 장고에서 이메일 보내기 위한 이메일 설정
# 이메일과 비밀번호 넣어두면 되는데 보안 문제로 2차 인증 활성화 해서 패스키 새로 만들어서 이용
# # (현재 '지웅'디바이스 등록되어 있어서 확인해보시고 싶으시면 자신 구글 아이디랑 비밀번호 넣으면 됩니다.)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Gmail SMTP 사용
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '***'  # 여기서 본인의 이메일 주소 입력
EMAIL_HOST_PASSWORD = '***'  # 여기서 본인의 이메일 비밀번호 입력
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

