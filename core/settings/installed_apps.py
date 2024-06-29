DJANGO_APPS = [
    'apps.contas',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_APPS = [
    "corsheaders",
]

PROJECT_APPS = [
    'apps.base',
    'apps.pages',
    'apps.perfil',
    'apps.config',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + PROJECT_APPS
