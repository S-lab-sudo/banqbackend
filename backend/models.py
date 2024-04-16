from django.db import models

# Create your models here.
class Reservation(models.Model):
    name=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=10)
    dateofvisit=models.DateField()
    noofguests=models.CharField(max_length=100)
    purposeofvisit=models.CharField(max_length=200)
    description=models.TextField()
    hallno=models.IntegerField(null=False,default=0)
    # TODO ADD CONSTRAINS (ONE DATE CAN HAVE ONLY 3 OR 1 TIME VISITS )
class Reviews(models.Model):
    username=models.CharField(max_length=100)
    emailaddress=models.EmailField(null=False,default=0)
    stars=models.IntegerField(null=False,default=5)
    description=models.TextField()
