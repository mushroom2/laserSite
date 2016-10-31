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