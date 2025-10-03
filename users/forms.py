
from django import forms
class UserForm(forms.Form):
    phone_number = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput())

