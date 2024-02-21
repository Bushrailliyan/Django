from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import TenantModelform, SignUpForm
from .models import Tenants,User_category,Member
from .models import ServiceProviders
from .forms import MemberModelform



# Create your views here.

def Register(request):
    try:
         form = SignUpForm(request.POST)
         if request.method == "POST":
              if form.is_valid():

                   form.save()
              return redirect('home')
         else:
              return render(request, 'signup.html', {'form': userform, 'msg': 'Invalid user'})
    except Exception as e:
         print(e)
         userform = SignUpForm()
         return render(request, 'signup.html', {'form': userform})


def login_page(request):
     try:
          username=request.POST.get('username')
          if request.user.is_authenticated:
               userGroup = Group.objects.get(user=request.user).name
               #print(userGroup)
               if userGroup=='Tenants':
                    return render(request,'tenant_login.html')
               elif userGroup=='ServiceProvider':
                    return render(request,'service_login.html')
          else:
               return render(request,'home.html')

     except Exception as e:
          print(e)
          return redirect('login')


def Loginview(request):
     username= request.POST.get('username')
     password = request.POST.get('password')
     user = authenticate(request,username=username,password=password)
     if user is not None:
          login(request,user)
          return redirect('loginpage')
     else:
          return render(request,'login.html',{'msg':'Invalid login'})


def Logout_view(request):
     logout(request)
     return redirect('home')

def home(request):
     return render(request,'home.html')

def about(request):
     return render(request,'about.html')

def Tenants_display(request):
     tenantdetls = Tenants.objects.all()
     return render(request,'tenants.html',{'tenantdetails':tenantdetls})

    #form = TenantModelform(request.POST,request.FILES)

def Servicepro(request):
     servicedetls  = ServiceProviders.objects.all()
     return render(request,'service_pro.html',{'servicedetails':servicedetls})


@login_required
def addmember(request):
     form = MemberModelform(request.POST)
     if request.method == "POST":

          if form.is_valid():
               form.save()
               return HttpResponse("Member Added")

     form = MemberModelform()
     return render(request, 'members.html', {'form': form})

@login_required
def display(request):
     #user_name=int(request.POST['tenant'])
     memberdtls = Member.objects.filter(user__id=request.user.id)
     return render(request,'members.html',{'memberdtls':memberdtls})



     # memberdtls = Members.objects.all()


@login_required
def update_member(request):
     oldname = request.POST.get("oldname")
     newname = request.POST.get("newname")
     membername = Member.objects.filter(name=oldname)
     if membername.exists():
          membername.update(name=newname)
          return render(request,'members.html',{'msg1':'updated'})
     else:
          return render(request, 'members.html', {'msg1': 'No records found'})
@login_required
def delete_member(request):
     memb_name = request.POST['name']
     memberobj = Member.objects.filter(name = memb_name)
     memberobj.delete()
     return render(request,'members.html',{'msg':'Deleted'})
@login_required
def goback_tenant(request):

     try:
          if request.user.is_authenticated:
               userGroup = Group.objects.get(user=request.user).name
               print(userGroup)
               if userGroup=='Tenants':
                    return render(request,'tenant_login.html')
               elif userGroup=='ServiceProvider':
                    return render(request,'service_login.html')
          else:
               return render(request,'home.html')

     except Exception as e:
          print(e)
          return redirect('login')












