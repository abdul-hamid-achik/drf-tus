# -*- coding: utf-8 -*-
from django.conf.urls import include
from django.urls import path

from rest_framework_tus.views import UploadViewSet

from .routers import TusAPIRouter

router = TusAPIRouter()
router.register(r'files', UploadViewSet, basename='upload')

urlpatterns = [
    path(r'', include((router.urls, 'rest_framework_tus'), namespace='api'))
]
app_name = 'rest_framework_tus'
