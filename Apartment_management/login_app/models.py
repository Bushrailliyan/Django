from django.db import models
from ResidentManager.models import House,HouseCategory,Tenants,ServiceCategory,ServiceProviders

# Create your models here.
STATUS_CHOICES = (
    ('assigned','ASSIGNED'),
    ('work progress','WORK PROGRESS'),
    ('done','DONE'),
)
REQUEST_CHOICES =(
    ('pending','PENDING'),
    ('cleared','CLEARED')
)
class ComplaintRequest(models.Model):
    service_needed =models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)
    tenant_name = models.ForeignKey(Tenants,on_delete=models.CASCADE)
    house = models.ForeignKey(House,on_delete=models.CASCADE)
    complaint_desc = models.CharField(max_length=250,default=None)
    request_status = models.CharField(max_length=8,choices=REQUEST_CHOICES,default=None)

class WorkStatus(models.Model):
    house_no = models.ForeignKey(House,on_delete=models.CASCADE,default=None)
    category = models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)
    name = models.ForeignKey(ServiceProviders,on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default=None)





