import os
import sys

from django.core.asgi import get_asgi_application

# Add project root directory to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "secureportal.settings")

django_app = get_asgi_application()

async def app(scope, receive, send):
    """
    Vercel ASGI entry point.
    MUST be named 'app' or Vercel will crash.
    """
    await django_app(scope, receive, send)
