

from django.contrib import admin
from blog.models import Article, Partners



#class PostAndDate(admin.TabularInline):
#    model = Article
 #   extra = 1


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'pub_day', 'w_p_r')
    #inlines = [PostAndDate]

admin.site.register(Article, PostAdmin)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('PartnerName', 'PartnerDate', 'PartnerPic')

admin.site.register(Partners, PartnerAdmin)
# Register your models here.
