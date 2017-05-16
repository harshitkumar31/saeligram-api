__author__ = "Harshit"

from django.conf.urls import url, include
from rest_framework import routers
from authentication.views import RequirementViewSet, BidViewSet, RequirementList, RequirementDetail, BidList, BidDetail, requirementById

router = routers.DefaultRouter()
router.register(r'requirements', RequirementViewSet)
router.register(r'bid', BidViewSet)

from .views import LoginAPIView, RegistrationAPIView
urlpatterns = [
    url(r'^users/?$', RegistrationAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
    url(r'^requirements/$', RequirementList.as_view()),
    url(r'^requirements/(?P<pk>\d+)$', RequirementDetail.as_view()),
    url(r'^v2/requirements/(?P<pk>\d+$)',requirementById),
    url(r'^bids/$', BidList.as_view()),
    url(r'^bids/(?P<pk>\d+)$', BidDetail.as_view()),

]

urlpatterns += router.urls