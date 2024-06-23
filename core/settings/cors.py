from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-Register',
]

# CORS Config
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_ALLOW_ALL como True, o que permite que qualquer site acesse seus
# recursos.
# Defina como False e adicione o site no CORS_ORIGIN_WHITELIST onde somente o
# site da lista acesse os seus recursos.


CORS_ALLOW_CREDENTIALS = False

CORS_ORIGIN_WHITELIST = [
    'http://meusite.com',
]  # Lista.
