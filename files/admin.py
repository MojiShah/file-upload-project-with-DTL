from django.contrib import admin
from .models import File
# Register your models here.

# admin.site.register(File)
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id','file','uploaded_at')
    list_display_links= ('id','file')
    ordering = ('-uploaded_at',)