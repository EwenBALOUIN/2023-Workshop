from django import forms

from .models import Customer
from .models import Action

class CustomerForm(forms.ModelForm):  
    class Meta:  
        model = Customer
        fields = ('first_name', 'name', 'email', 'mobile', 'address', 'status', 'company')

class ActionForm(forms.ModelForm):  
    class Meta:  
        model = Action
        fields = ('customer', 'action_type', 'description', 'scheduled_at', 'done_at')
