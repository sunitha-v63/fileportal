import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "secureportal.settings")

app = get_asgi_application()

async def handler(scope, receive, send):
    await app(scope, receive, send)
