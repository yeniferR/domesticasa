from django.conf.urls import url, include
from apps.cliente.views import cliente


urlpatterns = [
    url(r'^$', cliente,name='cliente'),
]