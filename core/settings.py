import os
from pathlib import Path
import re
# from django.core.exceptions import SuspiciousOperation

from django.conf.global_settings import ADMINS

# Защита от подделки заголовков Host
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Игнорирование сканирования уязвимостей
IGNORABLE_404_URLS = [
    re.compile(r"\.(php|asp|aspx|jsp|sql|git|env)$", re.IGNORECASE),
    #re.compile(r"/(admin|wp|wordpress|\.git)/"),
]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=*f8y@^sni8xu@kf4$%e4#qf6b921wq*e45+k%*y_qo*2fha@p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "*"]
# ALLOWED_HOSTS = [
# "guide-brewery.ru",
# "www.guide-brewery.ru",
# "guide-brewery.store",
# "www.guide-brewery.store",
# "82.202.131.133",
# ".82.202.131.133",
# "localhost",
# ".guide-brewery.ru",
# ".guide-brewery.store",  # Ловит поддомены, даже с ошибками
# ]

USER_AGENT_FILTER = [
    r"Googlebot",
    r"YandexBot",
    r"bingbot",
    r"XML Sitemaps",
    r"curl",
]
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "axes",  # Должно быть ПОСЛЕ 'django.contrib.admin'
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "django_extensions",
    "captcha",
    # "django_recaptcha",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "defender",
    "main",
    "route",
    "country",
    "brewery",
    "feedback",
    "django_cleanup",  # Должен быть добавлен ПОСЛЕ ваших приложений
]

SITE_ID = 1
# CAPTCHA_FLITE_PATH = r"C:\Program Files (x86)\eSpeak\command_line\espeak.exe"
CAPTCHA_CHALLENGE_FUNCT = "captcha.helpers.random_char_challenge" # Или текстовая с аудио:
# CAPTCHA_CHALLENGE_FUNCT = "captcha.helpers.math_challenge"  # Математическая капча
CAPTCHA_LENGTH = 4  # Количество символов
CAPTCHA_FONT_SIZE = 30  # Размер шрифта
CAPTCHA_IMAGE_SIZE = (170, 40)  # Размер изображения


AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesBackend",  # Должен быть ПЕРВЫМ
    "django.contrib.auth.backends.ModelBackend",
]

# Настройки блокировки
AXES_HANDLER = "axes.handlers.database.AxesDatabaseHandler"
AXES_FAILURE_LIMIT = 6  # Кол-во попыток перед блокировкой
AXES_COOLOFF_TIME = 1  # Блокировка на 1 час (можно timedelta(hours=1))
AXES_LOCKOUT_TEMPLATE = "account/lockout.html"  # Кастомный шаблон
AXES_RESET_ON_SUCCESS = True  # Сброс счетчика после успешного входа
AXES_USERNAME_FORM_FIELD = None  # Отключаем проверку по username
AXES_PASSWORD_FORM_FIELD = "pre_password"  # Указываем ваше поле пароля
AXES_LOCKOUT_PARAMETERS = [["ip_address", "user_agent"]]  # Блокировка по IP + браузеру


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "axes.middleware.AxesMiddleware",
    "defender.middleware.FailedLoginMiddleware",
]
# Снимаем любой запрет на блокировку curl, сканеры и т.д. - для Гугл и Яндекс ботов:
DISALLOWED_USER_AGENTS = []

DEFENDER_REDIS_URL = "redis://127.0.0.1:6379/0"

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "home",
        "USER": "home",
        "PASSWORD": "1111",
        "HOST": "localhost",
        "PORT": "5433",
    }
}

ADMINS = [
    ('', ''),
]


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = "/static/"
#STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # Для collectstatic
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]  # Ваши исходные статические файлы

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Важно для работы collectstatic
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATA_UPLOAD_MAX_NUMBER_FIELDS = None

# Email settings

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = "587"
EMAIL_USE_TLS = True

EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

EMAIL_SERVER = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = [""]

ADMIN_PRE_PASSWORD = ""  # для двухэтапного входа в админ-панель


# RECAPTCHA_PUBLIC_KEY = ""
# RECAPTCHA_PRIVATE_KEY = ""
