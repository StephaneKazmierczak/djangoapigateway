# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from . import views

app_name = 'apigateway'

urlpatterns = [
    url(r'.*', views.gateway.as_view())
]