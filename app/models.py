from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
from django.utils.translation import ugettext_lazy as _



class Hotel_Ticket(models.Model):
    price = models.CharField(max_length=30)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    img = models.ImageField()
    main_img = models.ImageField()
    desc1 = models.CharField(max_length=300)
    desc2 = models.CharField(max_length=300)


class Information(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=50)
    info_descrption = models.CharField(max_length=500)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name 



# class Rate(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL)
#     rate = models.PositiveIntegerField(null=False,blank=False)
#     hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE, null=True)
    

# class OrderHotel(models.Model):
#     hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL)
#     room = models.ForeignKey(Room, on_delete=models.SET_NULL)
#     order_date = models.DateTimeField(auto_now_add=True)
#     price = models.FloatField()
#     duration = models.CharField(max_length=30)


# class OrderTicket(models.Model):
#     ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL)
#     order_date = models.DateTimeField(auto_now_add=True)
#     price = models.FloatField()

#     def __str__(self):
#         return "Order ID: "+str(self.id)




# class RoomServices(models.Model):
#     curBooking = models.ForeignKey(OrderHotel,   null=True, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     createdDate = models.DateField(default=timezone.now)
#     servicesType = models.CharField(max_length=20, choices=SERVICES_TYPES)
#     price = models.FloatField()

#     def str(self):
#         return str(self.curBooking) + " " + str(self.room) + " " + str(self.servicesType)



# class Payment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL)
#     ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL)
#     price = models.CharField(max_length=30)




