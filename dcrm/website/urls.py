from django.urls import path
from . import views, admin

urlpatterns = [
    

path('', views.home, name="home"),
path('base/', views.base, name="base"),
path('login/', views.login_user, name="login"),
path('logout/', views.logout_user, name="logout"),
path('register/', views.register_user, name="register"),
path('registro/<int:pk>/', views.registro_cliente, name="registro"),
path('deletar_registro/<int:pk>/', views.deletar_registro, name="deletar_registro"),
path('registrar_cliente/', views.registrar_cliente, name="registrar_cliente"),
path('atualizar_registro/<int:pk>/', views.atualizar_registro, name="atualizar_registro"),
]