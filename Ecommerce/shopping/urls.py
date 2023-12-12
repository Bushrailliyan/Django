from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('edit',views.edit),
    path('accounts/login/',views.login_view,name='login'),
    path('logout',views.logout_view),
    path('accounts/sign_up/',views.sign_up,name = 'signup'),
    path('create',views.create,name='create'),
    path('dis',views.display),
    path('del',views.deleteitem),
    path('update',views.updateitem)

]