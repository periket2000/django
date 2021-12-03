from rest_framework.routers import DefaultRouter
from pdfs.api.views import PdfApiViewSet, PdfApiViewSet2

pdf_router = DefaultRouter()
pdf_router.register(prefix='pdfs', basename='pdfs', viewset=PdfApiViewSet)
pdf_router.register(prefix='pdfsbin', basename='pdfsbin', viewset=PdfApiViewSet2)
