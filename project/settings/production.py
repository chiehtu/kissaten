from .base import *


SECRET_KEY = get_env_var('SECRET_KEY')

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = get_env_var('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = get_env_var('EMAIL_HOST_PASSWORD')

EMAIL_PORT = 587

EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = ''

USERENA_USE_HTTPS = True
