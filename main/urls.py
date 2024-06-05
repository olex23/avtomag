from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.cars, name='cars'),
    path('cars/<int:id>/', views.car, name='car'),
    path('new_car/', views.new_car, name='new_car'),
    path('edit_car/<int:id>/', views.edit_car, name='edit_car'),
    path('profile/', views.profile, name='profile'),
    path('delete_car/<int:id>/', views.delete_car, name='delete_car'),

]