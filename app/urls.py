# from .views import RegisterAPI
from django.urls import path, include
# from knox import views as knox_views
from . import views
from rest_framework import routers

# router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'api', views.AuthViewSet, basename='api')



urlpatterns = [

    path('information/', views.information, name='information'),
    path('information-details/<int:pk>', views.information_details, name='information-details'),

    path('hotel-ticket/', views.hotel_ticket, name='hotel'),
    path('hotel_ticket-details/<int:pk>', views.hotel_ticket_details, name='hotel_ticket-details'),

    path('contact/', views.contact, name='contact'),
    
]
