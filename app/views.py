from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.http import HttpResponse 
from .utils import get_and_authenticate_user, create_user_account
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from django.contrib.auth import get_user_model, logout, login
from django.core.exceptions import ImproperlyConfigured
from rest_framework import generics, authentication, permissions, status, viewsets




@api_view(['GET', 'POST'])
def information(request):
    if request.method == 'GET':
        regions = Information.objects.all()
        serializer = InformationSerializer(regions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def information_details(request, pk):
    try:
        region = Information.objects.get(pk=pk)
    except Information.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'GET':
        serializer = InformationSerializer(region)
        return Response(serializer.data)
 
    elif request.method == 'PUT':
        serializer = InformationSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE':
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def hotel_ticket(request):
    if request.method == 'GET':
        regions = Hotel_Ticket.objects.all()
        serializer = Hotel_TicketSerializer(regions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Hotel_TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def hotel_ticket_details(request, pk):
    try:
        region = Hotel_Ticket.objects.get(pk=pk)
    except Hotel_Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'GET':
        serializer = Hotel_TicketSerializer(region)
        return Response(serializer.data)
 
    elif request.method == 'PUT':
        serializer = Hotel_TicketSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE':
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
def contact(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)







# @api_view(['GET', 'POST'])
# def rate(request):
#     if request.method == 'GET':
#         regions = Rate.objects.all()
#         serializer = RateSerializer(regions, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = RateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# def rate_details(request, pk):
#     try:
#         region = Rate.objects.get(pk=pk)
#     except Region.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
 
#     if request.method == 'GET':
#         serializer = RateSerializer(region)
#         return Response(serializer.data)
 
#     elif request.method == 'PUT':
#         serializer = RateSerializer(region, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
#     elif request.method == 'DELETE':
#         region.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET', 'POST'])
# def orderhotel(request):
#     if request.method == 'GET':
#         regions = OrderHotel.objects.all()
#         serializer = OrderHotelSerializer(regions, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = OrderHotelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# def orderhotel_details(request, pk):
#     try:
#         region = OrderHotel.objects.get(pk=pk)
#     except Region.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
 
#     if request.method == 'GET':
#         serializer = OrderHotelSerializer(region)
#         return Response(serializer.data)
 
#     elif request.method == 'PUT':
#         serializer = OrderHotelSerializer(region, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
#     elif request.method == 'DELETE':
#         region.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def orderticket(request):
#     if request.method == 'GET':
#         regions = OrderTicket.objects.all()
#         serializer = OrderTicketSerializer(regions, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = OrderTicketSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# def orderticket_details(request, pk):
#     try:
#         region = OrderTicket.objects.get(pk=pk)
#     except Region.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
 
#     if request.method == 'GET':
#         serializer = OrderTicketSerializer(region)
#         return Response(serializer.data)
 
#     elif request.method == 'PUT':
#         serializer = OrderTicketSerializer(region, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
#     elif request.method == 'DELETE':
#         region.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



















# @api_view(['GET', 'POST'])
# def airport(request):
#     if request.method == 'GET':
#         articles = Airport.objects.all()
#         serializer = AirportSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = AirportSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)



# @api_view(['GET', 'POST'])
# def images(request):
#     if request.method == 'GET':
#         articles = Images.objects.all()
#         serializer = ImagesSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ImagesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def flyfrom(request):
#     if request.method == 'GET':
#         articles = FlyFrom.objects.all()
#         serializer = FlyFromSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = FlyFromSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def ticket(request):
#     if request.method == 'GET':
#         articles = Ticket.objects.all()
#         serializer = TicketSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TicketSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def rate(request):
#     if request.method == 'GET':
#         articles = Rate.objects.all()
#         serializer = RateSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = RateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def service(request):
#     if request.method == 'GET':
#         articles = Service.objects.all()
#         serializer = ServiceSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ServiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def room(request):
#     if request.method == 'GET':
#         articles = Room.objects.all()
#         serializer = RoomSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = RoomSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def hotel(request):
#     if request.method == 'GET':
#         articles = Hotel.objects.all()
#         serializer = HotelSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = HotelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def order_ticket(request):
#     if request.method == 'GET':
#         articles = OrderTicket.objects.all()
#         serializer = OrderTicketSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = OrderTicketSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def order_hotel(request):
#     if request.method == 'GET':
#         articles = OrderHotel.objects.all()
#         serializer = OrderHotelSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = OrderHotelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)








