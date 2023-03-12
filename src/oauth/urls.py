from django.urls import path

from src.oauth.endpoint import auth_view, views

urlpatterns = [
    path('', auth_view.google_login),
    path('google/', auth_view.google_auth),
]

