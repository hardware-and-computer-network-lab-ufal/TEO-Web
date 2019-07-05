from django.urls import include, path
from rest_framework import routers
from restApi import views
from rest_framework.authtoken import views as viewsToken

router = routers.SimpleRouter()
router.register(r'api', views.PacienteViewSet)
# router.register(r'api-send', views.jogo_detail())

urlApiPattern = [
	path('api-token/', viewsToken.obtain_auth_token, name='api-token-auth'),
	path('api-jogos/', views.paciente_joga),
	path('api-gerais/', views.jogos_estatisticas),
]
urlApiPattern += router.urls