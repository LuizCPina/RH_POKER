from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vagas/', views.lista_vagas, name='lista_vagas'),
    path('vagas/<int:vaga_id>/', views.detalhes_vaga, name='detalhes_vaga'),
    path('vagas/<int:vaga_id>/candidatar/', views.candidatar, name='candidatar'),
    path('minhas_candidaturas/', views.minhas_candidaturas, name='minhas_candidaturas'),
]