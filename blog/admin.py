

from django.contrib import admin
from blog.models import Article



#class PostAndDate(admin.TabularInline):
#    model = Article
 #   extra = 1


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'pub_day', 'w_p_r')
    #inlines = [PostAndDate]





admin.site.register(Article, PostAdmin)

# Register your models here.
