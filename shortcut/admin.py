from django.contrib import admin
from shortcut.models import Shortcut 
# Register your models here.

@admin.register(Shortcut)
class ShortcutAdmin(admin.ModelAdmin):
    list_display = ('user','name', 'url', 'created_at', 'updated_at')
