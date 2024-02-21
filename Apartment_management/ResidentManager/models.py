from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User_category(AbstractUser):
    is_admin = models.BooleanField('Is admin',default=False)
    is_tenant = models.BooleanField('Is tenant',default=False)
    is_service = models.BooleanField('Is Service',default=False)

    def __str__(self):
        return self.username



class HouseCategory(models.Model):
    house_type = models.CharField(max_length=10)

    def __str__(self):
        return self.house_type

class House(models.Model):
    hs_no = models.CharField(max_length=6)
    hs_name = models.CharField(max_length=10)
    hs_type = models.ForeignKey(HouseCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.hs_no
class Tenants(models.Model):
    user_type = models.ForeignKey(User_category,on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=20)
    hs_no = models.ForeignKey(House,on_delete=models.CASCADE)
    mobile = models.BigIntegerField(null=True)
    id_proof =models.FileField(upload_to='images',default=None)

    def __str__(self):
        return self.name

    # def __str__(self):
    #     return f"{self.name} +'  '+ {self.hs_no}"

class ServiceCategory(models.Model):
    category = models.CharField(max_length=15)

    def __str__(self):
        return self.category



class ServiceProviders(models.Model):
    #user_type = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=250)
    service_category = models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)
    mobile = models.BigIntegerField(null=True)
    language_known = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images',default=None)

    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.ForeignKey(User_category,on_delete=models.CASCADE)
    t_name = models.ForeignKey(Tenants, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    relation = models.CharField(max_length=13)
    age = models.IntegerField(null=True)


