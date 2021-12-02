from rest_framework.serializers import ModelSerializer
from pdfs.models import Pdf


class PostPdfSerializer(ModelSerializer):
    class Meta:
        model = Pdf
        fields = ['title', 'description', 'pages']


class GetPdfSerializer(ModelSerializer):
    class Meta:
        model = Pdf
        fields = ['title', 'description', 'pages', 'created_at']
