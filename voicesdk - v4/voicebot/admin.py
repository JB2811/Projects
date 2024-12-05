from django.contrib import admin
from .models import Question, Answer, UserForm

admin.site.register(Question)
admin.site.register(Answer)

@admin.register(UserForm)
class UserFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'registration_number')
    search_fields = ('name', 'registration_number')