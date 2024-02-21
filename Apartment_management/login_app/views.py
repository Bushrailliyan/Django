from django.shortcuts import render,redirect

from .models import ComplaintRequest, ServiceCategory, Tenants, WorkStatus
from .forms import Complaintform,Statusform
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def Tenant_home(request):
    return render(request,'tenant_login.html')
@login_required
def members(request):
    return render(request,'members.html')
@login_required
def Goto_Request(request):
    return render(request, 'complaint.html')
@login_required
def Goto_Status(request):
    return render(request, 'status_view.html')
@login_required
def Goto_viewrequest(request):
    return render(request, 'request_view.html')
@login_required
def Goto_Putstatus(request):
    return render(request, 'status.html')
@login_required
def Go_to_Service(request):
    return render(request, 'service_login.html')
@login_required
def goto_login(request):
    return render(request,'homepage.html')

@login_required
def Complaint_Request(request):

    if request.method =="POST":
        form = Complaintform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'complaint.html',{'msg':"SENT"})

    form = Complaintform()
    return render(request, 'complaint.html', {'form': form})
@login_required
def Putstatus(request):
    if request.method =="POST":
        form = Statusform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'status.html',{'msg':"status added"})
    form = Statusform()
    return render(request,'status.html',{'form':form})

@login_required
def UpdateStatus(request):

    oldstatus = request.POST.get("oldchoice")
    newstatus = request.POST.get("newchoice")
    statusname = WorkStatus.objects.filter(status=oldstatus)
    if statusname.exists():
        statusname.update(status=newstatus)
        return render(request, 'status.html', {'msg1': 'updated'})
    else:
        return render(request, 'status.html', {'msg1': 'No records found'})
@login_required
def Status_view(request):
    status_reiview = WorkStatus.objects.all()
    return render(request,'status_view.html',{'statusview':status_reiview})
@login_required
def Request_view(request):
    complaint_view  = ComplaintRequest.objects.all()
    return render(request,'request_view.html',{'reqstview':complaint_view})










