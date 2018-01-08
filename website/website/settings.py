import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
try: 
    file = open("/secret/secretKey", "r") 
    SECRET_KEY = file.readline().replace('\n', '')
except:
    print("-- Note: the secret key file was not found and this server was started using the default key instead --")
    SECRET_KEY = '6*4$_taj=v6^1pa^c69vddq12+1x(8kgstr6izblpzi2@q7-6)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['178.62.111.52','metasophiea.eu','dev.metasophiea.eu']

ADMINS = [('Brandon', 'metasophiea@gmail.com')]

# Emails that the system wants to send, are printed to the console
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'stdout@metasophiea.eu'
EMAIL_HOST = '127.0.0.1'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
# SECURE_SSL_REDIRECT = True   # requireds HTTPS connection
# CSRF_COOKIE_SECURE = True    # requireds HTTPS connection
# SESSION_COOKIE_SECURE = True # requireds HTTPS connection
# SECURE_HSTS_SECONDS = 3600   # requireds HTTPS connection
X_FRAME_OPTIONS = 'DENY'
ROOT_URLCONF = 'website.urls'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
SOCIALACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'continuousverse.metasophiea.eu - '

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',

    'conVerse.apps.conVerse_config'
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'auth', 'templates', 'auth') ],
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

WSGI_APPLICATION = 'website.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'website',
        'USER': 'app',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': ''
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' }
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [
    "/website/auth/static"
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
