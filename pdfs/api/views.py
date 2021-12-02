from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pdfs.models import Pdf
from pdfs.api.serializers import GetPdfSerializer, PostPdfSerializer


class PostApiView(APIView):
    def get(self, request):
        # data = [pdf.title for pdf in Pdf.objects.all()]
        # return Response(status=status.HTTP_200_OK, data=data)
        serializer = GetPdfSerializer(Pdf.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        #Pdf.objects.create(title=request.data.get('title', ''),
        #                   description=request.data.get('description', ''),
        #                   pages=int(request.data.get('pages', '0'))
        #                   )
        serializer = PostPdfSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
