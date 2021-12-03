from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pdfs.models import Pdf
from pdfs.api.serializers import GetPdfSerializer, PostPdfSerializer
from rest_framework.viewsets import ViewSet
from pdfs.services.qr import Qr
from pdfs.services.pdf import Pdf as Pdfgen
from django.http import FileResponse


class PdfApiViewSet(ViewSet):
    def list(self, request):
        serializer = GetPdfSerializer(Pdf.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk):
        pdf = GetPdfSerializer(Pdf.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=pdf.data)

    def create(self, request):
        serializer = PostPdfSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        Qr.generate_qr(serializer.data.get("description", "https://www.google.es"))
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


class PdfApiViewSet2(ViewSet):
    def list(self, request):
        pdf_file = Pdfgen().generate_pdf(url="https://www.google.es", mesas=[1, 2, 3])
        pdf_file.output('/tmp/shit.pdf', 'F')
        return FileResponse(open('/tmp/shit.pdf', 'rb'), as_attachment=True, content_type='application/pdf')

# Before with APIViews, also impact on urls.py and router.py
# class PostApiView(APIView):
#     def get(self, request):
#         # data = [pdf.title for pdf in Pdf.objects.all()]
#         # return Response(status=status.HTTP_200_OK, data=data)
#         serializer = GetPdfSerializer(Pdf.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#     def post(self, request):
#         #Pdf.objects.create(title=request.data.get('title', ''),
#         #                   description=request.data.get('description', ''),
#         #                   pages=int(request.data.get('pages', '0'))
#         #                   )
#         serializer = PostPdfSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED, data=serializer.data)
