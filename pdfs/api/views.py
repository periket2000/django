from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pdfs.models import Pdf


class PostApiView(APIView):
    def get(self, request):
        data = [pdf.title for pdf in Pdf.objects.all()]
        return Response(status=status.HTTP_200_OK, data=data)
