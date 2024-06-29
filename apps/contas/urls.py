from django.urls import include, path

from contas import views


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path(
        'adicionar-usuario/',
        views.adicionar_usuario,
        name='adicionar_usuario'
    ),
    path(
        'atualizar-usuario/',
        views.atualizar_meu_usuario,
        name='atualizar_meu_usuario'
    ),
    path(
        'atualizar-usuario/<int:user_id>/',
        views.atualizar_usuario,
        name='atualizar_usuario'
    ),
    path('criar-conta/', views.register_view, name='register'),
    path('entrar/', views.login_view, name='login'),
    path('lista-usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path(
        'nova-senha/',
        views.force_password_change_view,
        name='force_password_change'
    ),
    path('sair/', views.logout_view, name='logout'),
    path('timeout/',  views.timeout_view, name='timeout'),
]
