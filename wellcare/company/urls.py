"""company URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^wellcare/home/$', views.get_homepage, name='homepage'),
    url(r'^wellcare/contacts/$', views.get_contact_info, name='contacts'),
    url(r'^wellcare/user/logout/$', views.user_logout, name='user_logout'),
    url(r'^wellcare/add/user_info/(?P<user_id>\d+)/$', views.add_user_informations, name='add_usr_info'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
