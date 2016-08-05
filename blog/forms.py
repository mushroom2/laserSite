from django import forms


class SimpleForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size': 40, 'class': 'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'size': 40, 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form- control'}))
    copy = forms.BooleanField(required=False)
