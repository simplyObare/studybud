from django.urls import path
from . import views


urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path("room/<str:pk>", views.getRoom, name="room"),
    path("rooms/", views.getRooms, name="rooms"),
]
