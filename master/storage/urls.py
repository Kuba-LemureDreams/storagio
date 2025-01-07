from django.urls import path
from . import views

urlpatterns = [
    path("items/", views.ListCreateItems.as_view()),
    path("items/<int:pk>/", views.RetrieveUpdateDeleteItems.as_view()),
    path("place/", views.ListCreatePlace.as_view()),
    path("place/<int:pk>/", views.RetrieveUpdateDeletePlace.as_view()),
    path("placement/", views.ListCreateItemPlaced.as_view()),
    path("placement/<int:pk>/", views.RetrieveUpdateDeletePlacement.as_view()),
    path("connect/", views.ListCreateUserPlacement.as_view()),
    path("connect/<int:pk>/", views.RetrieveUpdateDeleteUserPlacement.as_view()),
    path("register/", views.RegisterUser.as_view()),
    path("user-list/", views.ListUser.as_view()),
]
