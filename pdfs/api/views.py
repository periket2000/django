from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PostApiView(APIView):
    def get(self, request):
        data = {'name': 'Marco Albero', 'languages': ['python', 'java', 'react']}
        return Response(status=status.HTTP_200_OK, data=data)
