from django.shortcuts import render
from requests import Response

# Create your views here.

class ExampleAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello from Django!"})

    def post(self, request):
        data = request.data  # Data sent from the frontend
        return Response({"received": data})