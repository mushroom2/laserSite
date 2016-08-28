from django import forms
from magaz.models import *

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