from django.urls import path
from . import views

urlpatterns = [
    path('inscrever/', views.cadastro, name="inscrever"),
    path('login/', views.login, name='login'),
]
