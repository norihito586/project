from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser
from allauth.account.adapter import DefaultAccountAdapter

class CustomSignupForm(SignupForm):
    address = forms.CharField(label='住所', max_length=50, required=True)
    birth_day = forms.DateField(label='誕生日', required=True, widget=forms.DateInput(attrs={"type": "date"}),
                                                                      input_formats=['%Y-%m-%d'])
    field_order = ['username', 'email', 'address', 'birth_day', 'password1', 'password2']
    class Meta:
        model = CustomUser

    def signup(self, request,user):
        user.address = self.cleaned_data['address']
        user.birth_day = self.cleaned_data['birth_day']
        user.save()
        return user
