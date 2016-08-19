from django import forms
from magaz.models import MyUser


class CabinetForm(forms.Form):
    class Meta:
        model = MyUser
        fields = ('site', 'skype', 'profession', 'numb', 'about', 'avatar')
