from django import forms
from login_app.models import ComplaintRequest,WorkStatus


class Complaintform(forms.ModelForm):
    class Meta:
        model = ComplaintRequest
        fields = ['service_needed','tenant_name','house','complaint_desc','request_status']
        widgets = {
            'complaint_desc' :forms.Textarea()
        }

class Statusform(forms.ModelForm):
    class Meta:
        model = WorkStatus
        fields = ['category','name','status']

