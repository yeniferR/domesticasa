from django.conf.urls import url, include
from apps.servicios.views import servicios

urlpatterns = [
    url(r'^$', servicios,name='servicios'),
]
