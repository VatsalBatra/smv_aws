"""smv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import url, include, static
from django.contrib import admin
from django.conf import settings
from content import views as content_views
from .views import home

urlpatterns = [
    url(r'^$', content_views.first_page),
    url(r'^forum/$',content_views.forum,name = 'forum'),
    url(r'^forum/add/$',content_views.add,name = 'add'),
    url(r'^forum/content/$',content_views.content,name = 'content'),
    url(r'^forum/addans/$',content_views.add_ans,name = "addans"),
    url(r'^forum/upload/$',content_views.upload,name = "upload"),
    url(r'^admin/', admin.site.urls),
] + static.static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
