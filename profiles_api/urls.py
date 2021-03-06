from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserProfileViewSet, UserLoginApiView, UserProfileFeedViewSet

router = DefaultRouter()
router.register('profile', UserProfileViewSet)
router.register('feed', UserProfileFeedViewSet)

urlpatterns = [
     path('', include(router.urls)),
     path('login/', UserLoginApiView.as_view()),
]
