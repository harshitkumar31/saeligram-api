__author__ = "Harshit"

from datetime import datetime
from calendar import timegm
from rest_framework_jwt.settings import api_settings
from datetime import datetime, timedelta

def jwt_payload_handler(user):
    """ Custom payload handler
    Token encrypts the dictionary returned by this function, and can be decoded by rest_framework_jwt.utils.jwt_decode_handler
    """
    dt = datetime.now() + timedelta(days=60)
    return {
        'user_id': user.pk,
        'email': user.email,
        'is_superuser': user.is_superuser,
        'userType': user.userType,
        'exp': datetime.utcnow() + timedelta(days=30),
        'orig_iat': timegm(
            datetime.utcnow().utctimetuple()
        )
    }

def jwt_response_payload_handler(token, user=None, request=None):
    """ Custom response payload handler.

    This function controlls the custom payload after login or token refresh. This data is returned through the web API.
    """
    return {
        'user': {
             'email': user.email,
              'token': token,
              'userType': user.userType,
              'username': user.username,

        }
    }