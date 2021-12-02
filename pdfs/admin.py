from django.contrib import admin
from pdfs.models import Pdf


@admin.register(Pdf)
class PdfAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
