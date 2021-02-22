from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:category>', views.notice, name='notice'),
]
