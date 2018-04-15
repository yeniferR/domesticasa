"""emprendimiento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm,password_reset_complete
from apps.trabaja import views as trabaj_views
from apps.contacto import views  as contact_views
from apps.contratar import views as contrata_views




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('apps.home.urls',namespace='home')),
    url(r'^usuario/', include('apps.usuario.urls',namespace='usuario')),
    url(r'^limpieza/', include('apps.limpieza.urls',namespace='limpieza')),
    url(r'^login/', include('apps.login.urls',namespace= 'login')),
    url(r'^accounts/login/', login, {'template_name':'index.html'}, name= 'login'),
    url(r'^servicios/', include('apps.servicios.urls',namespace='servicios')),
    url(r'^preguntas/', include('apps.preguntas.urls',namespace='preguntas')),
    url(r'^cliente/', include('apps.cliente.urls',namespace='cliente')),
    url(r'^trabaja/$', trabaj_views.trabaja, name='trabaja'),
    url(r'^contratar/$', contrata_views.contratar, name='contratar'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^contacto/', contact_views.contacto, name='contacto'),
    url(r'^reset/password_reset', password_reset, 
        {'template_name':'registration/password_reset_form.html',
        'email_template_name': 'registration/password_reset_email.html'}, 
        name='password_reset'), 
    url(r'^password_reset_done', password_reset_done, 
        {'template_name': 'registration/password_reset_done.html'}, 
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, 
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),

    ]