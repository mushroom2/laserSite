from django.contrib import admin
from magaz.models import *


class CatAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'cat_pic', 'slag_url')

admin.site.register(Category, CatAdmin)

class ShopAdmin(admin.ModelAdmin):
    list_display = ('good_name', 'good_time', 'good_price', 'in_magaz')
    search_fields = ['good_name']


admin.site.register(Prises, ShopAdmin)


class SiteUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'site')
admin.site.register(SiteUser, SiteUserAdmin)


class SkypeUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'skype')
admin.site.register(SkypeUser, SkypeUserAdmin)


class ProfessionUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'profession')
admin.site.register(ProfessionalUser, ProfessionUserAdmin)


class NumbUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'numb')
admin.site.register(NumbUser, NumbUserAdmin)


class AboutUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'about')
admin.site.register(AboutUser,  AboutUserAdmin)


class AvatarUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
admin.site.register(AvatarUser, AvatarUserAdmin)