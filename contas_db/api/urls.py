from django.db import router
from django.urls import include, path
from .views import ContactViewSet

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', ContactViewSet),
    path('contact/<int:pk>/', ContactViewSet)
]
