from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('apartments/create/', views.apartment_create, name='apartment_create'),
    path('apartments/<str:apartment_code>/', views.apartment_detail, name='apartment_detail'),
]