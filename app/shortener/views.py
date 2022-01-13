from django.shortcuts import redirect, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest

from .models import ShortenLink


def redirect_to_url(request: WSGIRequest, link_key: str):
    link = get_object_or_404(ShortenLink, key=link_key)
    return redirect(link.link)
