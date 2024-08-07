from django.urls import path
from .views import *
urlpatterns = [
    path('myapp_index/',index),
    path('list/',list),
    path ('about/',about)
]
