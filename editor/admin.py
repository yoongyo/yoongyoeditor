from django.contrib import admin
from .models import Editor
from django import forms
from ckeditor.widgets import CKEditorWidget


class EditorAdmin(admin.ModelAdmin):
    content = forms.CharField(widget=CKEditorWidget)

    class Meta:
        model = Editor

    list_display = ['content']


admin.site.register(Editor, EditorAdmin)
