from django.conf.urls import url, include
from apps.limpieza.views import limpieza

urlpatterns = [
    url(r'^$', limpieza,name='limpieza'),
]