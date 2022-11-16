from django.contrib import admin
from django.urls import path
from principal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastroaluno/', cadastro_aluno, name='cadastro_aluno'),
]
