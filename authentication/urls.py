__author__ = "Harshit"

from django.conf.urls import url, include
from rest_framework import routers
from authentication.views import RequirementViewSet, BidViewSet

router = routers.DefaultRouter()
router.register(r'requirements', RequirementViewSet)
router.register(r'bid', BidViewSet)

from .views import LoginAPIView, RegistrationAPIView
urlpatterns = [
    url(r'^users/?$', RegistrationAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
]

urlpatterns += router.urls