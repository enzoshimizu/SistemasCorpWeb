import os

from core.settings.enviroment import BASE_DIR

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'

# STATICFILES_DIRS = [ # talvez em Produção podesse usar assim.
#     BASE_DIR / 'static',
# ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
