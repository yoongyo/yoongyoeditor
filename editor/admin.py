from django.contrib import admin
from .models import Editor


class EditorAdmin(admin.ModelAdmin):
    list_display = ['content']


admin.site.register(Editor, EditorAdmin)
