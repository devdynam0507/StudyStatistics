"""studystatement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from elections import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('elections.urls')),
    url('admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login_view, name='login'),
    url(r'^accounts/profile/$', views.index),
    url(r'^accounts/logout/$', auth_views.logout, name='logout', kwargs={'next_page': views.index})
] + static(settings.MEDIA_URL, document_ROOT=settings.MEDIA_ROOT)
