DEBUG = False

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ('127.0.0.1', 'localhost',)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "sidia",
        "USER": "postgres",
        "PASSWORD": "root",
        "HOST": "sidia_db",
        "PORT": "5433",
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'suporte@sidia.com.br'
EMAIL_HOST_PASSWORD = 'senha'
EMAIL_FROM_EMAIL = 'Suporte  <suporte@sidia.com.br>'
