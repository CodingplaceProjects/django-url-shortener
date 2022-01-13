from django.contrib import admin
from django.urls import path
from shortener import views as shortener_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<link_key>', shortener_views.redirect_to_url)
]
