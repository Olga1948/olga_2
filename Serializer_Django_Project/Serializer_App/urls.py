from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

urlpatterns = [
]

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns += router.urls
