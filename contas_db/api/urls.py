from django.urls import include, path
from .views import ContactViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('contacts/', ContactViewSet.as_view()),
    # path('contacts/<int:pk>/', ContactViewSet.as_view(), name='contact-detail'),
]