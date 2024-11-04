from django.contrib import admin
from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'user', 'encrypted_file', 'file_extension')  # Specify the fields to display in the list view
    search_fields = ('file_name', 'user__username')  # Enable searching by file name and username

admin.site.register(Document, DocumentAdmin)
