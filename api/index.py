import os
import sys
from django.core.asgi import get_asgi_application

# Add project root to PYTHONPATH (important for Vercel)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "secureportal.settings")

django_app = get_asgi_application()

async def handler(scope, receive, send):
    """
    Vercel serverless ASGI entrypoint.
    """
    await django_app(scope, receive, send)
