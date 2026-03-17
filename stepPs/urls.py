from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inscricao'),
    path('como-funciona/', views.como_funciona, name='como_funciona'),
]