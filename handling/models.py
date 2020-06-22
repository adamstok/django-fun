from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Equipments(models.Model):
    description = models.TextField()

    def __str__(self):
        return f'Description: {self.description}'
    def get_detail_url(self):
        return f'/equipements/{self.id}'


class Apartments(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    rented = models.BooleanField()
    equipment = models.ManyToManyField(Equipments, through='NumberOfEquipment')
    description = models.TextField()

    def __str__(self):
        return f'Name: {self.name} ; Address: {self.address}'
    def get_detail_url(self):
        return f'/apartments/{self.id}'


class NumberOfEquipment(models.Model):
    equipment = models.ForeignKey(Equipments,on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartments,on_delete=models.CASCADE)
    equipments_number = models.IntegerField(default=1)


class Renters(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    apartment = models.ForeignKey(Apartments,on_delete=models.CASCADE)

    def __str__(self):
        return f'First name: {self.first_name} ; Last name: {self.last_name} ; Apartment: {self.apartment}'
    def get_detail_url(self):
        return f'/renters/{self.id}'

class Payments(models.Model):
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=8, decimal_places=3)
    renter = models.ForeignKey(Renters, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartments,on_delete=models.CASCADE)

    def __str__(self):
        return f'Date: {self.date} ; Amount: {self.amount} ; Apartment: {self.apartment} ; Hirer: {self.renter}'
    def get_detail_url(self):
        return f'/payments/{self.id}'


