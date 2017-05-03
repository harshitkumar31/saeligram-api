from rest_framework import permissions

from SaeligramAPI import settings

__author__ = "Harshit"

import jwt


class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            print 'was safe'
            return True

        print 'Request', request

        try:
            auth = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
            x = jwt.decode(auth,settings.SECRET_KEY, algorithm='HS256')
            print x
            return x.get('userType') == 'B'
        except Exception as e :
            print e
            return False
        return False

    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     print 'was safe'
        #     return True

        print 'Request', request
        return False
