from django import forms
from magaz.models import *
from magaz.userdata import UserData

#общая "большая" форма
"""
class CabinetForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('site', 'skype', 'profession', 'numb', 'about', 'avatar')
"""

class SiteMiniForm(forms.ModelForm):
    class Meta:
        model = SiteUser
        fields = ('site',)


class SkypeMiniForm(forms.ModelForm):
    class Meta:
        model = SkypeUser
        fields = ('skype',)


class ProfessionMiniForm(forms.ModelForm):
    class Meta:
        model = ProfessionalUser
        fields = ('profession',)


class NumbMiniForm(forms.ModelForm):
    class Meta:
        model = NumbUser
        fields = ('numb',)


class AboutMiniForm(forms.ModelForm):
    class Meta:
        model = AboutUser
        fields = ('about',)


class AvatarMiniForm(forms.ModelForm):
    class Meta:
        model = AvatarUser
        fields = ('avatar',)


class PayGoodForm(forms.ModelForm):
    class Meta:
        model = GoodPay
        fields = []

class ValuteForm(forms.ModelForm):
    class Meta:
        model = Prises
        fields = ()

class HrivnaForm(forms.ModelForm):
    class Meta:
        model = Prises
        fields = ()

class OrderForm(forms.Form):
    ttt = [(1, 'нова пошта'), (2, 'самовивіз')]
    clientname = forms.CharField(required=True, label="Ім'я", widget=forms.TextInput(attrs={'size': 40,
                                                                                            'class': 'form-control'}))
    clientsorganization = forms.CharField(required=False, label="Організація")
    clientsnumb = forms.IntegerField(required=True, min_value=0)
    clientmail = forms.CharField(required=False, label='e-mail',
                                 widget=forms.TextInput(attrs={'size': 40, 'class': 'form-control'}))
    clientdevelop = forms.ChoiceField(choices=ttt)
    clientcomment = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))