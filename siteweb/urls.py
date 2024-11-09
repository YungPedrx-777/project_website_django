from django.urls import path
from . import views

#app_name = ""
urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    #path('', views.nav, name='nav'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('servicos/', views.servicos, name='servicos'),
     path('service_detail/<int:id>/', views.service_detail, name='service-detail'),
    
    
]