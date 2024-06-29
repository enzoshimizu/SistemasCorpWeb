from django.urls import path
from config import views

urlpatterns = [
    path('configuracao/', views.configuracao_view, name='configuracao'),
    path('', views.painel_view, name='painel'),
]
