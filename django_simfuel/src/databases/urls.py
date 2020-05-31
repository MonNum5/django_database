
from django.urls import path
from .views import registerDB, listCollections, updateDB, deleteDB
urlpatterns = [
    path('register/', registerDB),
    path('list/', listCollections, name='listDB'),
    path('<str:pk>', updateDB),
    path('<str:pk>/delete/', deleteDB),
]