from django.contrib import admin
from magaz.models import *


class CatAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'cat_pic', 'slag_url')

admin.site.register(Category, CatAdmin)

class ShopAdmin(admin.ModelAdmin):
    list_display = ('good_name', 'good_time', 'good_price', 'in_magaz')
    search_fields = ['good_name']


admin.site.register(Prises, ShopAdmin)

admin.site.register(SiteUser)
admin.site.register(SkypeUser)
admin.site.register(ProfessionalUser)
admin.site.register(NumbUser)
admin.site.register(AboutUser)
admin.site.register(AvatarUser)