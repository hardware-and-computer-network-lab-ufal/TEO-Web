from django.urls import path, include
from django.contrib.auth import views as auth_views
from usuario import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout, name='logout'),
    path('editar/', views.editar_perfil, name='editar_perfil'),
    path('recuperar-senha/formulario', auth_views.PasswordResetView.as_view(template_name='recuperar-senha/password_reset_form.html'), name='password_reset'),
    path('recuperar-senha/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='recuperar-senha/password_reset_confirm.html'), name='password_reset_confirm'),
    path('recuperar-senha/completo/', auth_views.PasswordResetDoneView.as_view(template_name='recuperar-senha/password_reset_done.html'), name='password_reset_done'),
    path('recuperar-senha/finalizado/', auth_views.PasswordResetCompleteView.as_view(template_name='recuperar-senha/password_reset_complete.html'), name='password_reset_complete'),
]
