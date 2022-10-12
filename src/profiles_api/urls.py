import profile
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from .views import (
    HelloAPIView,
    HelloViewSet,
    UserProfileViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename="hello-viewset")
router.register('profile', UserProfileViewSet)
router.register('login', LoginViewSet, basename='login')


urlpatterns = [
    path('hello/', HelloAPIView.as_view(), name='hello'),
    path(r'', include(router.urls), name="profile"),
] 

