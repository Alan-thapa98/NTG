from django.contrib import admin

# Register your models here.
from .models import *


# questions and answers for the learnesrs and educators

admin.site.register(which_grade)
admin.site.register(which_subject)
admin.site.register(which_author)
admin.site.register(which_subject_category)
admin.site.register(which_language)
admin.site.register(which_type)

@admin.register(answer_question)
class answer_questionAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)
