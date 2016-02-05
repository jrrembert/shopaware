"""shopaware_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib.auth.models import User
from django.contrib import admin

from rest_framework import routers, serializers, viewsets
from core.views import PlacesView, PlacesDetailView
from access.views import UserListView, UserDetailView

from rest_framework.urlpatterns import format_suffix_patterns

#
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
#router.register(r'places', views.PlacesViewSet)

# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^admin/', admin.site.urls),
#     url(r'^access/', include('rest_framework.urls'), name='access')
# ]


urlpatterns = [
    url(r'^users/$', UserListView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailView.as_view()),
    url(r'^places/$', PlacesView.as_view()),
    url(r'^places/(?P<pk>[0-9]+)/$', PlacesDetailView.as_view()),
    url(r'^access/', include('rest_framework.urls'), name='access')
]

urlpatterns = format_suffix_patterns(urlpatterns)
