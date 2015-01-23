from django.contrib import admin

# Register your models here.

#from polls.models import Question

#admin.site.register(Question)
from polls.models import Question,Choice


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('hi',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)