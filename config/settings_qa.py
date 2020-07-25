from .settings import *  # noqa

DEBUG = True
EMAIL_DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa

MEDIA_ROOT = os.path.join(BASE_DIR, 'test_media')  # noqa

DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'
