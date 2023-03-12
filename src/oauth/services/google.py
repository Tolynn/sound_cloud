from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from src.oauth.models import AuthUser
from src.oauth.serializer import GoogleAuth
from google.oauth2 import id_token
from google.auth.transport import requests
from .base_auth import create_token, create_access_token

def check_google_auth(google_user: GoogleAuth) -> dict:
    try:
        id_token.verify_token(google_user['token'], requests.Request, settings.GOOGLE_CLIENT_ID)
    except ValueError:
        raise AuthenticationFailed(code=403, detail='BAd token Google')

    user, _ = AuthUser.objects.get_or_create(email=google_user['email'])
    return create_token(user_id=user.id)