from django import forms
from magaz.models import MyUser

#общая "большая" форма
"""
class CabinetForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('site', 'skype', 'profession', 'numb', 'about', 'avatar')
"""

class SiteMiniForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('site',)


class SkypeMiniForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('skype',)


class ProfessionMiniForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('profession',)


class NumbMiniForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('numb',)


class AboutMiniForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('about',)


class AvatarMiniForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('avatar',)