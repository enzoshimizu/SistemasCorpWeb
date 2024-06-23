from django.urls import path
from apps.pages import views

urlpatterns = [
    path('', views.index, name='home'),
]
