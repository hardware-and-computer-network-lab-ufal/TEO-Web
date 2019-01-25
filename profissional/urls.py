from django.urls import path
from profissional import views

urlpatterns = [
    path('novo/', views.novo_profissional, name='novo_profissional'),
    path('listar/', views.listar_profissional, name='listar_profissionais'),
    path('atualizar/<cpf>/', views.atualizar_profissional, name='atualizar_profissional'),
    path('deletar/<cpf>/', views.deletar_profissional, name='deletar_profissional'),
]
