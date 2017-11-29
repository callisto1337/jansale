from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.main),
    url(r'^category/(?P<url>[A-Za-z]+)/$', views.category)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
