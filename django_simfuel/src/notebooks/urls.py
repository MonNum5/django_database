from django.urls import path
from .views import notebooksList, notebooksView, stopNotebook
urlpatterns = [
    path('', notebooksList, name='notebookList'),
    path('notebook/', notebooksView),
    path('notebook/stop/', stopNotebook),
]