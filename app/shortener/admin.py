from django.contrib import admin
from .models import ShortenLink


@admin.register(ShortenLink)
class ShortenLinkAdmin(admin.ModelAdmin):
    list_display = ("__str__", "shorten_link", )
    readonly_fields = ("shorten_link", )
