from django.contrib import admin

from django.contrib import admin

from .models import Choice, Question



class QuestionAndChoice(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("вопрос",               {'fields': ['question_text']}),
        ('когда опубликован', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [QuestionAndChoice]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)


