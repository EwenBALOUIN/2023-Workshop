from django import forms

from .models import Customer
from .models import Action
from .models import Company
from django.contrib.auth.models import User

class CustomerForm(forms.ModelForm):  
    class Meta:  
        model = Customer
        fields = ('first_name', 'name', 'email', 'mobile', 'address', 'status', 'company')

class ActionForm(forms.ModelForm):  
    class Meta:  
        model = Action
        fields = ('customer', 'action_type', 'description', 'scheduled_at', 'done_at')

class CompanyForm(forms.ModelForm):  
    class Meta:  
        model = Company
        fields = ('name', 'address')

class UserForm(forms.ModelForm):  
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        # password readonly
        widgets = {
            'password': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
