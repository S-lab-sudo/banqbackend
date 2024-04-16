from django.contrib import admin
from django.urls import path
from backend import views

urlpatterns = [
    path('',views.home),
    path('makereservation',views.makeReservation),
    path('checkdates',views.getAvailableDates),
    path('addreviews',views.addreviews),
    path('getreviews',views.getreviews),
    path('get_csrf_token',views.get_csrf_token),
]
