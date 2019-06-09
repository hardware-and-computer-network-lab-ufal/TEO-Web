from django.urls import include, path
from rest_framework import routers
from restApi import views
from rest_framework.authtoken import views as viewsToken

router = routers.DefaultRouter()
router.register(r'api', views.PacienteViewSet)


urlApiPattern = [
	path('', include(router.urls)),
	path('api-token-auth/', viewsToken.obtain_auth_token, name='api-token-auth')
]