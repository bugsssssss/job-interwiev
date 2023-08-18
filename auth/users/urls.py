from django.urls import path
from .views import *
from rest_framework import routers


urlpatterns = [
    path("", home, name="home"),
    path('auth/', Authorization.as_view(), name='auth'),
    path('code/', Authenticate.as_view(), name='code'),
    path('invite/', ActivateInvite.as_view(), name='invite'),
    path('user/', GetUserDetail.as_view(), name='user')
]
