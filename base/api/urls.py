from django.urls import path
from . import views


urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path("rooms/<str:pk>", views.getRoom, name="sub-room"),
    path("rooms/", views.getRooms, name="rooms"),
]
