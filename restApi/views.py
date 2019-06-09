from django.shortcuts import render
from paciente.models import Paciente
from rest_framework import viewsets
from restApi.serializers import PacienteSerializer

# Create your views here.
class PacienteViewSet(viewsets.ModelViewSet):
	queryset = Paciente.objects.all()
	serializer_class = PacienteSerializer

# class UserView():
# 	data = serializers.serialize("json", User.objects.get(username='admin'))
