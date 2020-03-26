from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Editor(models.Model):
    content = RichTextUploadingField(blank=True,
                                     null=True,
                                     external_plugin_resources=[(
                                         'youtube',
                                         '/static/base/vendor/ckeditor_plugins/youtube/youtube/',
                                         'plugin.js',
                                     )])