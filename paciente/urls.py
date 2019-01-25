from django.urls import path
from paciente import views

urlpatterns = [
    path('novo/', views.novo_paciente, name='novo_paciente'),
    path('listar/', views.listar_paciente, name='listar_pacientes'),
    path('atualizar/<cpf>/', views.atualizar_paciente, name='atualizar_paciente'),
    path('deletar/<cpf>/', views.deletar_paciente, name='deletar_paciente'),
    path('perfil/<cpf>/', views.perfil_paciente, name='perfil_paciente'),
]
