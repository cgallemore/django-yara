from django.conf import settings
settings.configure(
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": 'yara.db'
            }
    },
    INSTALLED_APPS=[
        "django.contrib.auth",
        "yara",
    ],
)
from django.test import TestCase


class TestCase(TestCase):
    pass