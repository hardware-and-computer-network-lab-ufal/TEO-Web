from django.urls import path
from clinica import views

urlpatterns = [
    path('nova/', views.nova_clinica, name='nova_clinica'),
    path('lista/', views.listar_clinica, name='listar_clinicas'),
    path('atualizar/<cnpj>/', views.atualizar_clinica, name='atualizar_clinica'),
    path('deletar/<cnpj>/', views.deletar_clinica, name='deletar_clinica'),
]
