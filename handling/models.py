from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ApartmentsRooms(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return f'Name: {self.name}'
    def get_detail_url(self):
        return f'/rooms/{self.id}/'
    def get_edit(self):
        return f'/rooms/edit/{self.id}/'
    def get_delete(self):
        return f'/rooms/delete/{self.id}/'

class Apartments(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    surface = models.DecimalField(max_digits=8, decimal_places=3)
    rent = models.IntegerField(null=True)
    costs = models.IntegerField(null=True)
    rooms = models.ManyToManyField(ApartmentsRooms)
    equipment = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'Name: {self.name} ; Address: {self.address}'
    def get_detail_url(self):
        return f'/apartments/{self.id}/'
    def get_edit(self):
        return f'/apartments/edit/{self.id}/'
    def get_delete(self):
        return f'/apartments/delete/{self.id}/'




class Renters(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    apartment = models.ForeignKey(Apartments,on_delete=models.CASCADE)

    def __str__(self):
        return f'First name: {self.first_name} ; Last name: {self.last_name} '#; Apartment: {self.apartment}'
    def get_detail_url(self):
        return f'/renters/{self.id}/'
    def get_edit(self):
        return f'/renters/edit/{self.id}/'
    def get_delete(self):
        return f'/renters/delete/{self.id}/'

class Payments(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=3)
    renter = models.ForeignKey(Renters, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartments,on_delete=models.CASCADE)

    def __str__(self):
        return f'Date: {self.date} ; Amount: {self.amount} ; Apartment: {self.apartment} ; Hirer: {self.renter}'
    def get_detail_url(self):
        return f'/payments/{self.id}/'
    def get_edit(self):
        return f'/payments/edit/{self.id}/'
    def get_delete(self):
        return f'/payments/delete/{self.id}/'


class ExamplePic(models.Model):
    model_pic = models.ImageField(upload_to='pic_folder/',default='pic_folder/None/no-img.jpg')


class ApartmentsPics(models.Model):
    pics = models.ImageField(upload_to='pic_folder/',default='pic_folder/None/no-img.jpg')
    apartment = models.ForeignKey(Apartments,on_delete=models.CASCADE)
    def get_delete(self):
        return f'/pictures/delete/{self.id}/'
    def get_apartment(self):
        return f'/apartments/{self.apartment_id}/'
