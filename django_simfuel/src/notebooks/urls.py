from django.urls import path
from .views import notebooksList, notebooksView, createNotebook
urlpatterns = [
    path('', notebooksList, name='notebookList'),
    path('notebook/', notebooksView),
    path('create/', createNotebook),
]