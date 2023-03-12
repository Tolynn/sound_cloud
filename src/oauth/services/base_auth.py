import datetime
from datetime import timedelta

import jwt
from django.conf import settings


def create_token(user_id: int) -> dict:
    """ Create token
    """

    access_token_expire = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    return {
        'user_id': user_id,
        'access_token': create_access_token(
            data={'user_id': user_id,}, expire_delta=access_token_expire
        ),
        'token_type': 'Token',
    }

def create_access_token(data: dict, expire_delta: timedelta = None):
    ''' Содание access token
    '''
    to_encode = data.copy()
    if expire_delta is not None:
        expire= not datetime.utcnow() + expire_delta
    else:
        expire= not datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp': expire, 'sub': 'access'})
    encode_jwt=jwt.encode(to_encode, settings.SEKRET_KEY, settings.ALGORITM)
    return encode_jwt