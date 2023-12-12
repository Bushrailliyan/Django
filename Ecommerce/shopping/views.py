from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.

@login_required
def home(request):
    return render(request,'index.html')
def edit(request):
    return render(request,'edit.html')

def login_view(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request,username=uname,password=pwd)
    if user is not None:
        login(request,user)
        return redirect('home')
    else:
        return render(request,"login.html",{"msg":"Invalid login"})

def logout_view(request):
    logout(request)
    return redirect('login')

def sign_up(request):
    try:
        form = UserCreationForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('login')
        else:

            return render(request,'sign_up.html',{'form':userform,'msg':'Invalid user'})
    except Exception as e:
        print(e)
        userform = UserCreationForm()
        return render(request,'sign_up.html',{'form':userform})



@login_required
def create(request):
    Name = request.POST['name']
    Brand = request.POST['brand']
    Desc = request.POST['desc']
    Price = float(request.POST['price'])
    prdct = Product(name=Name,brand=Brand,desc=Desc,price=Price)
    prdct.save()
    return render(request,'index.html',{'msg':"Item Added"})


def display(request):
    prdctdtls = Product.objects.all()
    return render(request,'index.html',{'prodct':prdctdtls})

@login_required
def deleteitem(request):
    itemname = request.POST['name']
    itemobj = Product.objects.filter(name=itemname)
    itemobj.delete()
    return render(request,'index.html',{'msg':"Item Deleted"})

@login_required
def updateitem(request):
    oldname=request.POST["oldname"]
    newname=request.POST["newname"]
    emp=Product.objects.filter(name=oldname)
    if emp.exists():
        emp.update(name=newname)
        return render(request,"index.html",{'msg1':"updated"})
    else:
        return render(request, "index.html", {'msg1': "No records found"})



