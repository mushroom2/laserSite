from django import forms
from registration.forms import User


class SimpleForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size': 40, 'class': 'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'size': 40, 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    copy = forms.BooleanField(required=False)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

