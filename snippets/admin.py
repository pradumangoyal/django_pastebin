from django.contrib import admin
from snippets.models import Snippet, Comment
# Register your models

admin.site.register(Snippet)
admin.site.register(Comment)
