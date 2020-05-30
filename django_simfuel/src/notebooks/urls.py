from django.urls import path
from .views import notebooksList
urlpatterns = [
    path('', notebooksList),
]