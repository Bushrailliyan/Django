from django.contrib import admin
from .models import HouseCategory
from .models import Tenants
from .models import House
from .models import ServiceCategory
from .models import ServiceProviders,User_category,Member
from django.contrib.auth import get_user_model


# Register your models here.
# class ResidentAdmin(admin.ModelAdmin):
#     list_display = ['id','name','flat','mobile','id_proof']
#     ordering = ('flat',)
#     search_fields = ('name','flat')
admin.site.register(get_user_model())
admin.site.register(House)
admin.site.register(Tenants)
admin.site.register(HouseCategory)
admin.site.register(ServiceCategory)
admin.site.register(ServiceProviders)
admin.site.register(Member)