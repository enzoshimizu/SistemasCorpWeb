import os

from core.settings.enviroment import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, os.getenv('NAME_DB')),
        # 'USER':os.getenv('USER_DB')
        # 'PASSWORD': os.getenv('PASSWORD_DB')
        # 'HOST':os.getenv('HOST_DB')
        # 'PORT':os.getenv('PORT_DB')

    }
}
