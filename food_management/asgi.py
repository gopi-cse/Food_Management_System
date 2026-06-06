"""ASGI config for async-capable deployment servers."""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "food_management.settings")
application = get_asgi_application()
