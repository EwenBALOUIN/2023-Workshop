from django import forms

from .models import Customer
from .models import Action
from django.contrib.auth.models import User

class CustomerForm(forms.ModelForm):  
    class Meta:  
        model = Customer
        fields = ('first_name', 'name', 'email', 'mobile', 'address', 'status', 'company')

class ActionForm(forms.ModelForm):  
    class Meta:  
        model = Action
        fields = ('customer', 'action_type', 'description', 'scheduled_at', 'done_at')

class UserForm(forms.ModelForm):  
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }
