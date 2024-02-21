from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Tenants,User_category,Member


class SignUpForm(UserCreationForm):
    class Meta:
        model = User_category
        fields = ['username','password1','password2','is_admin','is_tenant','is_service']

class TenantModelform(forms.ModelForm):
    class Meta:
        model = Tenants
        fields = '__all__'
        # OR can use fields = ['name','flat','mobile','id_proof']


class MemberModelform(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'