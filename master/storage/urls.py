from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.ListCreateItems.as_view()),
    path('place/', views.ListCreatePlace.as_view()),
    path('placement/', views.ListCreateItemPlaced.as_view()),
    path('register/', views.RegisterUser.as_view()),
    path('login/', views.LoginView.as_view()),
    path('user-list/', views.ListUser.as_view()),
]
