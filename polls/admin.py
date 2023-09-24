from django.contrib import admin

from .models import Questions, Choice

admin.site.site_header = 'The CybersForth Academy'
admin.site.site_title = 'The CybersForth polls'
admin.site.index_title = 'Welcome to the CybersForth Poll admin area'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
              ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

admin.site.register(Questions, QuestionAdmin)
