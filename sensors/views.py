from django.shortcuts import render
from rest_framework import viewsets
from .models import Sensor, Data, Alert
from .serializers import SensorSerializer, DataSerializer, AlertSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse


class ExampleView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request):
        content = {'message': f'auth, {request.user.username}!'}
        return Response(content)


def login_view(request):
    return render(request, 'login.html')


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


def oauth_callback(request):
    # Your code here
    return HttpResponse("OAuth callback response")


class ExampleView(APIView):
    """
    retrieve:
    Return a single item by ID.

    list:
    Return all items.

    This endpoint allows for retrieving all items or a single item by its ID.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Optional detailed description for the GET method.

        Retrieves the list of items or a single item if an ID is provided.
        Parameters:
            - request: The incoming HTTP request.
            - format: Specifies the format of the response (optional).

        Returns a Response object with the list of items.
        """
        items = ["item1", "item2", "item3"]  # Example list of items
        return Response(items)
