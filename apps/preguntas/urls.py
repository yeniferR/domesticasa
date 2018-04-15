from django.conf.urls import url, include
from apps.preguntas.views import preguntas

urlpatterns = [
    url(r'^$', preguntas,name='preguntas'),
]
