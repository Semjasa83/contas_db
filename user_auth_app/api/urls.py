from django.urls import include, path
from .views import RegistrationView

from rest_framework import routers

#router = routers.SimpleRouter()
#router.register(r'', RegistrationViewSet)

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    # path('activate/<str:token>/', activate_user, name='activate_user'),
]