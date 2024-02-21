from django.urls import path
from. import views
from ResidentManager.views import *


urlpatterns = [
    #path('',views.home,name='home'),
    path('',views.Tenant_home,name ='tenantpage'),
    #path('/login/',Loginview,name='login'),
    #path('accounts/profile/',login_page,name='loginpage'),
    path('goto',views.goto_login,name='gotologin'),
    path('create',addmember,name='member'),
    path('dis',display,name='dis'),
    path('update',update_member,name='update'),
    path('del',delete_member,name='del'),
    path('service_login',views.Go_to_Service,name='servicepage'),
    path('putstatus',views.Putstatus),
    path('complaint',views.Goto_Request),
    path('status',views.Goto_Status),
    path('statusview',views.Status_view),
    path('addcompl',views.Complaint_Request),
    path('member',views.members),
    path('reqst',views.Goto_viewrequest),
    path('reqstview',views.Request_view),
    path('put',views.Goto_Putstatus)
    ]