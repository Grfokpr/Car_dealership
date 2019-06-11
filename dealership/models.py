from django.db import models

# Create your models here.


class Dealership(models.Model):
    name = models.CharField(max_length=255)

class Car(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    dealership = models.ForeignKey(Dealership,on_delete=models.CASCADE, )
    color = models.CharField(max_length=255)
    price = models.FloatField()
    engine_m3 = models.FloatField()


    def create_car(self):
        pass

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)