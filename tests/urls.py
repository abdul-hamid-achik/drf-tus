# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import include
from django.urls import path

from rest_framework_tus.urls import urlpatterns as rest_framework_tus_urls

urlpatterns = [
    path('tus', include(rest_framework_tus_urls)),
]
