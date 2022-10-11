from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import HelloAPIView, HelloViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename="hello-viewset")

urlpatterns = [
    path('hello/', HelloAPIView.as_view(), name='hello'),
    path('', include(router.urls))
]