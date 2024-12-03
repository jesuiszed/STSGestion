from django.urls import path
from . import views

urlpatterns = [
    path('reloading/', views.home0, name='home0'),
    path('employe/', views.employe, name='home'),
    path('adminPage/', views.adminPage, name='home1'),
    # path('accueil/', views.accueil, name='home'),
    #path('chart/', views.chart, name='home'),
    path('export_voyages/', views.export_voyages_to_excel, name='export_voyages'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ajouter_voyage/', views.ajout_voyage, name='ajout_voyage'),
    path('modifier_voyage/<int:pk>/', views.modifier_voyage, name='modifier_voyage'),
    path('supprimer_voyage/<int:pk>/', views.supprimer_voyage, name='supprimer_voyage'),
    #path('export-voyages/', views.export_voyages_to_excel, name='export_voyages'),

]