from django.urls import path
from . import views

urlpatterns = [
    path('', views.deptos_list, name='deptos_list'),
    path('search',views.search_deptos, name='search_deptos'),
    path('deptos', views.new_deptos_list, name='new_deptos_list'),
    path('selected', views.selected_list, name='selected_list')
]