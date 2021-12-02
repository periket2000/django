from rest_framework.routers import DefaultRouter
from pdfs.api.views import PdfApiViewSet

pdf_router = DefaultRouter()
pdf_router.register(prefix='pdfs', basename='pdfs', viewset=PdfApiViewSet)