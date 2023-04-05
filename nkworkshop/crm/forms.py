from django import forms

from .models import Customer
from .models import Action
from .models import Company
from .models import Message
from django.contrib.auth.models import User

class CustomerForm(forms.ModelForm):
    company = forms.CharField()
    class Meta:  
        model = Customer
        fields = ('first_name', 'name', 'email', 'mobile', 'address', 'status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO: fix company field for creation/update
        if self.instance.pk:
            test = Company.objects.filter(contacts__pk=self.instance.pk)
            if test:
                self.fields['company'].initial = test[0].name
            else:
                self.fields['company'].initial = 'Pas de société'
            self.fields['company'].widget.attrs['readonly'] = True

class ActionForm(forms.ModelForm):  
    class Meta:  
        model = Action
        fields = ('customer', 'action_type', 'description', 'scheduled_at', 'done_at')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['scheduled_at'].widget.attrs['class'] = 'datetimeinput'
            self.fields['scheduled_at'].initial = self.instance.scheduled_at.strftime('%Y-%m-%dT%H:%M')
            self.fields['done_at'].widget.attrs['class'] = 'datetimepicker'
            self.fields['done_at'].initial = self.instance.done_at.strftime('%Y-%m-%dT%H:%M')


class CompanyForm(forms.ModelForm):
    contacts = forms.ModelMultipleChoiceField(
        queryset=Customer.objects.all(),
        widget=forms.SelectMultiple,
        required=False,
    )

    class Meta:  
        model = Company
        fields = ('name', 'address', 'contacts')

class UserForm(forms.ModelForm):  
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        # password readonly
        widgets = {
            'password': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

class MessageForm(forms.ModelForm):  
    class Meta:
        model = Message
        fields = ('user', 'action', 'content')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        action_id = kwargs.get('initial', {}).get('action_id', None)
        if action_id:
            action = Action.objects.filter(id=action_id).values_list('id', flat=True).first()
            self.fields['action'].initial = action

        user_id = kwargs.get('initial', {}).get('user_id', None)
        if user_id:
            user = User.objects.filter(id=user_id).values_list('id', flat=True).first()
            self.fields['user'].initial = user