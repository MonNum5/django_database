from django.urls import path
from .views import notebooksList, notebooksView, createNotebook, updateNotebook, deleteNotebook

urlpatterns = [
    path('', notebooksList, name='notebookList'),
    path('notebook/', notebooksView),
    path('create/', createNotebook),
    path('<str:pk>', updateNotebook),
    path('<str:pk>/delete/', deleteNotebook),
    path('<str:pk>/start/', notebooksView),
]