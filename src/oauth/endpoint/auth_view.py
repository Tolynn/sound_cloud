from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from ..serializer import GoogleAuth
from ..services.google import check_google_auth


def google_login(request):
    '''Страница входа через гугл
    '''
    return render(request, 'oauth/google_login.html')

@api_view(["POST"])
def google_auth(request):
    '''Подтвержение авторзации через гугл
    '''

    google_data= GoogleAuth(data=request.data)
    if google_data.is_valid():
        token=check_google_auth(google_data.data)
        return Response(token)
    else:
        return AuthenticationFailed(code=403, detail='Bad data Google!')
