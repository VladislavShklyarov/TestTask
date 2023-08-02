from django.urls import path

from .views import *

urlpatterns = [
    path('', UserInfo, name="UserInfo"),
    path('success/', success, name = 'success',)
]