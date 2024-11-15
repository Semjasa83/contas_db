from django.urls import include, path
from .views import ContactViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', ContactViewSet),
    path('contact/<int:pk>/', ContactViewSet)
]