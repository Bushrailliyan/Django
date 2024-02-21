from django.contrib import admin
from .models import ComplaintRequest,WorkStatus

# Register your models here.
admin.site.register(ComplaintRequest)
admin.site.register(WorkStatus)

