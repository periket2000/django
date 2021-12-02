from django.contrib import admin
from pdfs.models import Pdf


# make it appear in http://localhost:8000/admin manager
@admin.register(Pdf)
class PdfAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
