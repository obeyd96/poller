from django.contrib import admin

from .models import Question, Choices

admin.site.site_header = "Poller Admin"
admin.site.site_title = "Poller Admin Area"
admin.site.index_title = "Poller Index"


class ChoiceInline(admin.TabularInline):
    model = Choices
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['q_text']}),
                 ('Date Information', {'fields': ['published'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
# admin.site.register(Choices)
