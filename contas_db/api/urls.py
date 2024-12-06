from django.urls import path, include
from .views import ContactViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]