from django.urls import include, path
from .views import ContactViewSet, NoteViewSet

from rest_framework import routers

contact_router = routers.SimpleRouter()
contact_router.register(r'contacts', ContactViewSet)

note_router = routers.SimpleRouter()
note_router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(contact_router.urls)),
    path('', include(note_router.urls)),
]