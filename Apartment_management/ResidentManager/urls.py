from django.urls import path
from login_app.views import *
from .import views

urlpatterns = [
    path('',views.home,name ='home'),
    path('signup/',views.Register,name = 'signup'),
    path('accounts/login/',views.Loginview,name = 'login'),
    path('accounts/profile/',views.login_page,name='loginpage'),
    path('accounts/profile/signout',views.Logout_view,name='signout'),
    path('accounts/profile/member',members,name='memberdetails'),
    path('about/',views.about,name='about'),
    path('tenants',views.Tenants_display,name='tenants'),
    path('providers',views.Servicepro,name='providers'),
    path('accounts/profile/create',views.addmember,name ='member'),
    path('accounts/profile/dis',views.display,name='dis'),
    path('accounts/profile/update',views.update_member),
    path('accounts/profile/del',views.delete_member),
    path('accounts/profile/addcompl',Complaint_Request),
    path('accounts/profile/complaint',Goto_Request),
    path('putstatus',Putstatus),
    path('accounts/profile/status',Goto_Status),
    path('accounts/profile/statusview', Status_view),
    path('accounts/profile/reqst',Goto_viewrequest),
    path('accounts/profile/reqstview',Request_view),
    path('accounts/profile/put',Goto_Putstatus),
    path('accounts/profile/putstatus',Putstatus),
    path('accounts/profile/updatestatus',UpdateStatus),
    path('accounts/profile/back',views.goback_tenant)

]